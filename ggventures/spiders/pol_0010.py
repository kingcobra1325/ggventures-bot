import scrapy


class Pol0010Spider(scrapy.Spider):
    name = 'pol_0010'
    allowed_domains = ['https://www.postgrad.com/institution/wielkopolska-business-school/6678/']
    start_urls = ['http://https://www.postgrad.com/institution/wielkopolska-business-school/6678//']

    def parse(self, response):
        pass
