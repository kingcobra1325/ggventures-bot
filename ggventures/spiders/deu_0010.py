import scrapy


class Deu0010Spider(scrapy.Spider):
    name = 'deu_0010'
    allowed_domains = ['https://www.wiwiss.fu-berlin.de/en/index.html']
    start_urls = ['http://https://www.wiwiss.fu-berlin.de/en/index.html/']

    def parse(self, response):
        pass
