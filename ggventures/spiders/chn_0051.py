import scrapy


class Chn0051Spider(scrapy.Spider):
    name = 'chn_0051'
    allowed_domains = ['http://english.zjgsu.edu.cn/']
    start_urls = ['http://http://english.zjgsu.edu.cn//']

    def parse(self, response):
        pass
