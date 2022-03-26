import scrapy


class Ind0044Spider(scrapy.Spider):
    name = 'ind_0044'
    allowed_domains = ['https://www.tiss.edu/']
    start_urls = ['http://https://www.tiss.edu//']

    def parse(self, response):
        pass
