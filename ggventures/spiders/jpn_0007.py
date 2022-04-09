import scrapy


class Jpn0007Spider(scrapy.Spider):
    name = 'jpn_0007'
    allowed_domains = ['https://www.kansai-u.ac.jp/English/']
    start_urls = ['http://https://www.kansai-u.ac.jp/English//']

    def parse(self, response):
        pass
