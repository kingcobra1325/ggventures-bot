import scrapy


class Aus0032Spider(scrapy.Spider):
    name = 'aus_0032'
    allowed_domains = ['https://www.uwa.edu.au/schools/Business']
    start_urls = ['http://https://www.uwa.edu.au/schools/Business/']

    def parse(self, response):
        pass
