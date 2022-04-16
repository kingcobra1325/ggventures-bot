import scrapy


class Nld0013Spider(scrapy.Spider):
    name = 'nld_0013'
    allowed_domains = ['https://www.rug.nl/about-ug/how-to-find-us/find-an-expert?lang=en']
    start_urls = ['http://https://www.rug.nl/about-ug/how-to-find-us/find-an-expert?lang=en/']

    def parse(self, response):
        pass
