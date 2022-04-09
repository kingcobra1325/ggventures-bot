import scrapy


class Ita0016Spider(scrapy.Spider):
    name = 'ita_0016'
    allowed_domains = ['https://www.unipa.it/scuole/politecnica/economia/index.html']
    start_urls = ['http://https://www.unipa.it/scuole/politecnica/economia/index.html/']

    def parse(self, response):
        pass
