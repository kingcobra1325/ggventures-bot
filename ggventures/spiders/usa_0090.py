import scrapy


class Usa0090Spider(scrapy.Spider):
    name = 'usa_0090'
    allowed_domains = ['https://www.ut.edu/academics/sykes-college-of-business']
    start_urls = ['http://https://www.ut.edu/academics/sykes-college-of-business/']

    def parse(self, response):
        pass
