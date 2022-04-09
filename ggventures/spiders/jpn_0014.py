import scrapy


class Jpn0014Spider(scrapy.Spider):
    name = 'jpn_0014'
    allowed_domains = ['https://english.rikkyo.ac.jp/']
    start_urls = ['http://https://english.rikkyo.ac.jp//']

    def parse(self, response):
        pass
