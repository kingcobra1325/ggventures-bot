import scrapy


class Chn0032Spider(scrapy.Spider):
    name = 'chn_0032'
    allowed_domains = ['https://en.sjtu.edu.cn/']
    start_urls = ['http://https://en.sjtu.edu.cn//']

    def parse(self, response):
        pass
