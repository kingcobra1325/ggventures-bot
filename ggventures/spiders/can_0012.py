import scrapy


class Can0012Spider(scrapy.Spider):
    name = 'can_0012'
    allowed_domains = ['https://www.usherbrooke.ca/']
    start_urls = ['http://https://www.usherbrooke.ca//']

    def parse(self, response):
        pass
