import scrapy


class Jpn0019Spider(scrapy.Spider):
    name = 'jpn_0019'
    allowed_domains = ['https://www.mbaib.gsbs.tsukuba.ac.jp/']
    start_urls = ['http://https://www.mbaib.gsbs.tsukuba.ac.jp//']

    def parse(self, response):
        pass
