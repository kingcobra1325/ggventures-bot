import scrapy


class Jpn0012Spider(scrapy.Spider):
    name = 'jpn_0012'
    allowed_domains = ['https://www.meiji.ac.jp/cip/english/']
    start_urls = ['http://https://www.meiji.ac.jp/cip/english//']

    def parse(self, response):
        pass
