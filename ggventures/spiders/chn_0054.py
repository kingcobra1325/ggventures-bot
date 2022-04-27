import scrapy


class Chn0054Spider(scrapy.Spider):
    name = 'chn_0054'
    allowed_domains = ['http://www.sysu.edu.cn/']
    start_urls = ['http://http://www.sysu.edu.cn//']

    def parse(self, response):
        pass
