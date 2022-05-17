import scrapy


class Rus0001Spider(scrapy.Spider):
    name = 'rus_0001'
    allowed_domains = ['https://find-mba.com/schools/europe/russia/ranepa-gsib']
    start_urls = ['http://https://find-mba.com/schools/europe/russia/ranepa-gsib/']

    def parse(self, response):
        pass
