import random
import html2text
import scrapy
import boto3
try:
    from tutorial import dynamoDB
except:
    import dynamoDB


class WikiSpider(scrapy.Spider):
    name = "wiki"
    start_urls = ["http://en.wikipedia.org/wiki/Python_(programming_language)",
                  "https://en.wikipedia.org/wiki/Game",
                  "https://en.wikipedia.org/wiki/Queen%27s_University_Belfast"]

    def parse(self, response):

        record = self.build_record(response)
        self.store_page(record)

        links = self.get_links(response)

        links_to_search = list()
        for i in range(5):  # choose 5 random links
            links_to_search.append(random.choice(links))
        self.store_links(links_to_search)

        next_link = self.get_random_link()
        yield scrapy.Request(next_link, callback=self.parse)
        next_link = self.get_random_link()
        yield scrapy.Request(next_link, callback=self.parse)

    def get_random_link(self):
        table = dynamoDB.get_table('Links')
        records = table.scan(AttributesToGet=['URL'])['Items']
        link = random.choice(records)['URL']
        table.delete_item(
            Key={
                'URL': link,
            })
        return link

    def get_links(self, response):
        wiki_links = list()
        links = response.css('a::attr(href)').getall()
        for link in links:
            if(link.startswith('/wiki/')):
                if(not link.startswith('/wiki/Wikipedia:')):
                    wiki_link = response.urljoin(link)
                    wiki_links.append(wiki_link)
        return wiki_links

    def build_record(self, response):
        record = dict()
        record['URL'] = response.request.url

        body = response.css("body").get()
        converter = html2text.HTML2Text()
        converter.ignore_links = True
        text = converter.handle(body)
        record['text'] = text

        record['title'] = response.css('title::text').get()
        return record

    def store_page(self, record):
        table = dynamoDB.get_table('Indexing')
        table.put_item(Item=record)

    def store_links(self, links):
        table = dynamoDB.get_table('Links')
        for link in links:
            table.put_item(Item={'URL': link})
