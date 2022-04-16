import scrapy


class Pol0006Spider(scrapy.Spider):
    name = 'pol_0006'
    allowed_domains = ['https://www.educations.com/study-abroad/polish-open-university/']
    start_urls = ['http://https://www.educations.com/study-abroad/polish-open-university//']

    def parse(self, response):
        pass
