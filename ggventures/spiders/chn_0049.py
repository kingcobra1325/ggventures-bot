import scrapy


class Chn0049Spider(scrapy.Spider):
    name = 'chn_0049'
    allowed_domains = ['https://free-apply.com/en/articles/country/1814991/city/11120158']
    start_urls = ['http://https://free-apply.com/en/articles/country/1814991/city/11120158/']

    def parse(self, response):
        pass
