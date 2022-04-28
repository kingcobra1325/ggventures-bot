import scrapy


class Chn0052Spider(scrapy.Spider):
    name = 'chn_0052'
    allowed_domains = ['https://www.zju.edu.cn/english/']
    start_urls = ['http://https://www.zju.edu.cn/english//']

    def parse(self, response):
        pass
