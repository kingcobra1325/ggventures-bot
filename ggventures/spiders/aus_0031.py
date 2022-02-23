import scrapy


class Aus0031Spider(scrapy.Spider):
    name = 'aus_0031'
    allowed_domains = ['https://www.usc.edu.au/about/structure/schools/school-of-business-and-creative-industries']
    start_urls = ['http://https://www.usc.edu.au/about/structure/schools/school-of-business-and-creative-industries/']

    def parse(self, response):
        pass
