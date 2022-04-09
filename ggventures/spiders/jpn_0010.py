import scrapy


class Jpn0010Spider(scrapy.Spider):
    name = 'jpn_0010'
    allowed_domains = ['https://www.econ.kyoto-u.ac.jp/en/']
    start_urls = ['http://https://www.econ.kyoto-u.ac.jp/en//']

    def parse(self, response):
        pass
