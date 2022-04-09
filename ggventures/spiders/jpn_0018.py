import scrapy


class Jpn0018Spider(scrapy.Spider):
    name = 'jpn_0018'
    allowed_domains = ['https://www.tus.ac.jp/en/fac/keiei/']
    start_urls = ['http://https://www.tus.ac.jp/en/fac/keiei//']

    def parse(self, response):
        pass
