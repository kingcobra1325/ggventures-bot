import scrapy


class Aus0011Spider(scrapy.Spider):
    name = 'aus_0011'
    allowed_domains = ['https://www.mq.edu.au/about/about-the-university/our-faculties/business/study-with-us/mgsm']
    start_urls = ['http://https://www.mq.edu.au/about/about-the-university/our-faculties/business/study-with-us/mgsm/']

    def parse(self, response):
        pass
