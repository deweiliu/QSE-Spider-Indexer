# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM ubuntu

# If you prefer miniconda:
#FROM continuumio/miniconda3

LABEL Name=qse-indexing Version=0.0.1

WORKDIR /app
ADD . /app

RUN apt-get update 
RUN apt-get --assume-yes install python3

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -y install gcc mono-mcs
RUN rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
RUN pytest
RUN scrapy crawl wiki
CMD ["scrapy crawl wiki"]

# Using pipenv:
#RUN python3 -m pip install pipenv
#RUN pipenv install --ignore-pipfile
#CMD ["pipenv", "run", "python3", "-m", "qse-searching"]

# Using miniconda (make sure to replace 'myenv' w/ your environment name):
#RUN conda env create -f environment.yml
#CMD /bin/bash -c "source activate myenv && python3 -m qse-searching"
