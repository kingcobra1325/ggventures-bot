import scrapy


class Chn0047Spider(scrapy.Spider):
    name = 'chn_0047'
    allowed_domains = ['http://en.xjtu.edu.cn/']
    start_urls = ['http://http://en.xjtu.edu.cn//']

    def parse(self, response):
        pass
