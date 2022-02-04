import scrapy


class Aus0027Spider(scrapy.Spider):
    name = 'aus_0027'
    allowed_domains = ['https://usq.edu.au/bela/school-of-business']
    start_urls = ['http://https://usq.edu.au/bela/school-of-business/']

    def parse(self, response):
        pass
