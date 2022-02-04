import scrapy


class Aus0017Spider(scrapy.Spider):
    name = 'aus_0017'
    allowed_domains = ['https://www.swinburne.edu.au/australian-graduate-school-of-entrepreneurship/']
    start_urls = ['http://https://www.swinburne.edu.au/australian-graduate-school-of-entrepreneurship//']

    def parse(self, response):
        pass
