import scrapy


class Chn0044Spider(scrapy.Spider):
    name = 'chn_0044'
    allowed_domains = ['https://en.ustc.edu.cn/']
    start_urls = ['http://https://en.ustc.edu.cn//']

    def parse(self, response):
        pass
