import scrapy


class Jpn0009Spider(scrapy.Spider):
    name = 'jpn_0009'
    allowed_domains = ['https://b.kobe-u.ac.jp/en/']
    start_urls = ['http://https://b.kobe-u.ac.jp/en//']

    def parse(self, response):
        pass
