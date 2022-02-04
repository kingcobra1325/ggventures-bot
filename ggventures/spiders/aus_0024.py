import scrapy


class Aus0024Spider(scrapy.Spider):
    name = 'aus_0024'
    allowed_domains = ['https://www.canberra.edu.au/about-uc/faculties/busgovlaw/canberra-business-school-cbs']
    start_urls = ['http://https://www.canberra.edu.au/about-uc/faculties/busgovlaw/canberra-business-school-cbs/']

    def parse(self, response):
        pass
