import scrapy


class Gbr0020Spider(scrapy.Spider):
    name = 'gbr_0020'
    allowed_domains = ['https://www.mmu.ac.uk/business-school/']
    start_urls = ['http://https://www.mmu.ac.uk/business-school//']

    def parse(self, response):
        pass
