import scrapy


class Can0023Spider(scrapy.Spider):
    name = 'can_0023'
    allowed_domains = ['https://www.uvic.ca/gustavson/']
    start_urls = ['http://https://www.uvic.ca/gustavson//']

    def parse(self, response):
        pass
