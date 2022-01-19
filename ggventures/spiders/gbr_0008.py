import scrapy


class Gbr0008Spider(scrapy.Spider):
    name = 'gbr_0008'
    allowed_domains = ['https://www.coventry.ac.uk/study-at-coventry/faculties-and-schools/coventry-business-school/']
    start_urls = ['http://https://www.coventry.ac.uk/study-at-coventry/faculties-and-schools/coventry-business-school//']

    def parse(self, response):
        pass
