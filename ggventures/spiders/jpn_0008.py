import scrapy


class Jpn0008Spider(scrapy.Spider):
    name = 'jpn_0008'
    allowed_domains = ['http://www.kbs.keio.ac.jp/en/']
    start_urls = ['http://http://www.kbs.keio.ac.jp/en//']

    def parse(self, response):
        pass
