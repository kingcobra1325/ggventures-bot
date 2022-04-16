import scrapy


class Nld0005Spider(scrapy.Spider):
    name = 'nld_0005'
    allowed_domains = ['https://www.msm.nl/']
    start_urls = ['http://https://www.msm.nl//']

    def parse(self, response):
        pass
