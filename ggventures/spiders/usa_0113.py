import scrapy


class Usa0113Spider(scrapy.Spider):
    name = 'usa_0113'
    allowed_domains = ['https://www.hartford.edu/academics/schools-colleges/barney/default.aspx']
    start_urls = ['http://https://www.hartford.edu/academics/schools-colleges/barney/default.aspx/']

    def parse(self, response):
        pass
