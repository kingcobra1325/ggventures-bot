import scrapy


class Jpn0011Spider(scrapy.Spider):
    name = 'jpn_0011'
    allowed_domains = ['https://www.econ.kyushu-u.ac.jp/english/index/']
    start_urls = ['http://https://www.econ.kyushu-u.ac.jp/english/index//']

    def parse(self, response):
        pass
