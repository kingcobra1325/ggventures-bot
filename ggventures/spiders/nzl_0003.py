import scrapy


class Nzl0003Spider(scrapy.Spider):
    name = 'nzl_0003'
    allowed_domains = ['https://www.massey.ac.nz/massey/explore/departments/massey-business-school/massey-business-school_home.cfm']
    start_urls = ['http://https://www.massey.ac.nz/massey/explore/departments/massey-business-school/massey-business-school_home.cfm/']

    def parse(self, response):
        pass
