import scrapy


class Jpn0013Spider(scrapy.Spider):
    name = 'jpn_0013'
    allowed_domains = ['https://www.nucba.ac.jp/en/']
    start_urls = ['http://https://www.nucba.ac.jp/en//']

    def parse(self, response):
        pass
