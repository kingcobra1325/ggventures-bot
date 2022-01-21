import scrapy


class Gbr0030Spider(scrapy.Spider):
    name = 'gbr_0030'
    allowed_domains = ['https://www.bath.ac.uk/schools/school-of-management/']
    start_urls = ['http://https://www.bath.ac.uk/schools/school-of-management//']

    def parse(self, response):
        pass
