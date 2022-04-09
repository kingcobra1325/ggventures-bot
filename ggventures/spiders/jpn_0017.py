import scrapy


class Jpn0017Spider(scrapy.Spider):
    name = 'jpn_0017'
    allowed_domains = ['https://www.econ.tohoku.ac.jp/english/page-graduate.html']
    start_urls = ['http://https://www.econ.tohoku.ac.jp/english/page-graduate.html/']

    def parse(self, response):
        pass
