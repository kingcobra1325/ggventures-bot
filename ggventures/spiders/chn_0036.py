import scrapy


class Chn0036Spider(scrapy.Spider):
    name = 'chn_0036'
    allowed_domains = ['https://en.scut.edu.cn/']
    start_urls = ['http://https://en.scut.edu.cn//']

    def parse(self, response):
        pass
