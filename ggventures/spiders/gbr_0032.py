import scrapy


class Gbr0032Spider(scrapy.Spider):
    name = 'gbr_0032'
    allowed_domains = ['https://www.jbs.cam.ac.uk/']
    start_urls = ['http://https://www.jbs.cam.ac.uk//']

    def parse(self, response):
        pass
