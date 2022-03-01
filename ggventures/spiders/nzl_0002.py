import scrapy


class Nzl0002Spider(scrapy.Spider):
    name = 'nzl_0002'
    allowed_domains = ['https://www.lincoln.ac.nz/study/study-programmes/programme-search/bachelor-of-commerce-agriculture/']
    start_urls = ['http://https://www.lincoln.ac.nz/study/study-programmes/programme-search/bachelor-of-commerce-agriculture//']

    def parse(self, response):
        pass
