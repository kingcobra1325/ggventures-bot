import scrapy


class Usa0049Spider(scrapy.Spider):
    name = 'usa_0049'
    allowed_domains = ['https://www.middlebury.edu/institute/events']
    start_urls = ['http://https://www.middlebury.edu/institute/events/']

    def parse(self, response):
        pass
