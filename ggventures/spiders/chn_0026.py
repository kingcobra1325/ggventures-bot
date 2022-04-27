import scrapy


class Chn0026Spider(scrapy.Spider):
    name = 'chn_0026'
    allowed_domains = ['https://english.pku.edu.cn/']
    start_urls = ['http://https://english.pku.edu.cn//']

    def parse(self, response):
        pass
