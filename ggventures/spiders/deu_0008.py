import scrapy


class Deu0008Spider(scrapy.Spider):
    name = 'deu_0008'
    allowed_domains = ['https://businesspf.hs-pforzheim.de/en/']
    start_urls = ['http://https://businesspf.hs-pforzheim.de/en//']

    def parse(self, response):
        pass
