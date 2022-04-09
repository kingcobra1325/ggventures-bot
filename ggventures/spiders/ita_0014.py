import scrapy


class Ita0014Spider(scrapy.Spider):
    name = 'ita_0014'
    allowed_domains = ['https://milano.unicatt.it/facolta/economia']
    start_urls = ['http://https://milano.unicatt.it/facolta/economia/']

    def parse(self, response):
        pass
