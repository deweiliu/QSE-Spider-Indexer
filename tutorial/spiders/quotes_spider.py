import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com'
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'pages/quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        for quote in response.css('div.row div.quote'):
            json = dict()
            json['author'] = quote.css('small.author::text').get()
            json['text'] = quote.css('span.text::text').get()
            json['tags'] = quote.css('div.tags a.tag::text').getall()
            yield json

        next_pages = response.css("ul.pager li.next a::attr(href)").getall()
        for next_page in next_pages:   
            print(next_page)
            yield response.follow(next_page, callback=self.parse)
