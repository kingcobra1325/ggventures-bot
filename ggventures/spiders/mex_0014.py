import scrapy


class Mex0014Spider(scrapy.Spider):
    name = 'mex_0014'
    allowed_domains = ['https://www.yumpu.com/en/document/view/39384375/pc-384-oto-07-universidad-de-las-amacricas-a-c']
    start_urls = ['http://https://www.yumpu.com/en/document/view/39384375/pc-384-oto-07-universidad-de-las-amacricas-a-c/']

    def parse(self, response):
        pass
