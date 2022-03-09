import scrapy


class Fra0045Spider(scrapy.Spider):
    name = 'fra_0045'
    allowed_domains = ['https://www.iae-paris.com/en/international/sorbonne-business-school']
    start_urls = ['http://https://www.iae-paris.com/en/international/sorbonne-business-school/']

    def parse(self, response):
        pass
