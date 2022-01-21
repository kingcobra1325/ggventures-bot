import scrapy


class Gbr0021Spider(scrapy.Spider):
    name = 'gbr_0021'
    allowed_domains = ['https://www.mdx.ac.uk/about-us/what-we-do/faculty-of-professional-and-social-sciences/business-school']
    start_urls = ['http://https://www.mdx.ac.uk/about-us/what-we-do/faculty-of-professional-and-social-sciences/business-school/']

    def parse(self, response):
        pass
