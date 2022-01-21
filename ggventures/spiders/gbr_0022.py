import scrapy


class Gbr0022Spider(scrapy.Spider):
    name = 'gbr_0022'
    allowed_domains = ['https://www.napier.ac.uk/about-us/our-schools/the-business-school']
    start_urls = ['http://https://www.napier.ac.uk/about-us/our-schools/the-business-school/']

    def parse(self, response):
        pass
