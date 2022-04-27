import scrapy


class Chn0034Spider(scrapy.Spider):
    name = 'chn_0034'
    allowed_domains = ['http://english.sxu.edu.cn/']
    start_urls = ['http://http://english.sxu.edu.cn//']

    def parse(self, response):
        pass
