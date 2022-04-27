import scrapy


class Chn0029Spider(scrapy.Spider):
    name = 'chn_0029'
    allowed_domains = ['https://english.snnu.edu.cn/']
    start_urls = ['http://https://english.snnu.edu.cn//']

    def parse(self, response):
        pass
