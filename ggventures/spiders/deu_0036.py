import scrapy


class Deu0036Spider(scrapy.Spider):
    name = 'deu_0036'
    allowed_domains = ['https://www.zeppelin-university.com/']
    start_urls = ['http://https://www.zeppelin-university.com//']

    def parse(self, response):
        pass
