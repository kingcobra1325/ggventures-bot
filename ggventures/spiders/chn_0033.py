import scrapy


class Chn0033Spider(scrapy.Spider):
    name = 'chn_0033'
    allowed_domains = ['https://english.sufe.edu.cn/']
    start_urls = ['http://https://english.sufe.edu.cn//']

    def parse(self, response):
        pass
