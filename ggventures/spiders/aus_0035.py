import scrapy


class Aus0035Spider(scrapy.Spider):
    name = 'aus_0035'
    allowed_domains = ['https://www.vu.edu.au/about-vu/our-teaching-colleges-schools/victoria-university-business-school']
    start_urls = ['http://https://www.vu.edu.au/about-vu/our-teaching-colleges-schools/victoria-university-business-school/']

    def parse(self, response):
        pass
