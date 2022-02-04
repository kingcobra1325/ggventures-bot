import scrapy


class Aus0003Spider(scrapy.Spider):
    name = 'aus_0003'
    allowed_domains = ['https://www.cqu.edu.au/about-us/structure/schools/bl']
    start_urls = ['http://https://www.cqu.edu.au/about-us/structure/schools/bl/']

    def parse(self, response):
        pass
