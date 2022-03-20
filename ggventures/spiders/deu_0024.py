import scrapy


class Deu0024Spider(scrapy.Spider):
    name = 'deu_0024'
    allowed_domains = ['https://www.uni-goettingen.de/en/faculty+of+economic+sciences/356424.html']
    start_urls = ['http://https://www.uni-goettingen.de/en/faculty+of+economic+sciences/356424.html/']

    def parse(self, response):
        pass
