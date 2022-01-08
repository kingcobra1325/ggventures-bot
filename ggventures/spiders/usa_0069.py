import scrapy


class Usa0069Spider(scrapy.Spider):
    name = 'usa_0069'
    allowed_domains = ['https://www.stjohns.edu/academics/schools/peter-j-tobin-college-business']
    start_urls = ['http://https://www.stjohns.edu/academics/schools/peter-j-tobin-college-business/']

    def parse(self, response):
        pass
