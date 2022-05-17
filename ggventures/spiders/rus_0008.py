import scrapy


class Rus0008Spider(scrapy.Spider):
    name = 'rus_0008'
    allowed_domains = ['https://free-apply.com/en/university/1064300265']
    start_urls = ['http://https://free-apply.com/en/university/1064300265/']

    def parse(self, response):
        pass
