import scrapy


class Gbr0027Spider(scrapy.Spider):
    name = 'gbr_0027'
    allowed_domains = ['https://www.rgu.ac.uk/study/academic-schools/aberdeen-business-school']
    start_urls = ['http://https://www.rgu.ac.uk/study/academic-schools/aberdeen-business-school/']

    def parse(self, response):
        pass
