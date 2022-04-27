import scrapy


class Chn0038Spider(scrapy.Spider):
    name = 'chn_0038'
    allowed_domains = ['https://e.swufe.edu.cn/']
    start_urls = ['http://https://e.swufe.edu.cn//']

    def parse(self, response):
        pass
