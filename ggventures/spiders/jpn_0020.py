import scrapy


class Jpn0020Spider(scrapy.Spider):
    name = 'jpn_0020'
    allowed_domains = ['https://www.waseda.jp/top/en/']
    start_urls = ['http://https://www.waseda.jp/top/en//']

    def parse(self, response):
        pass
