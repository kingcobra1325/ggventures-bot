import scrapy


class Can0010Spider(scrapy.Spider):
    name = 'can_0010'
    allowed_domains = ['https://www.smu.ca/academics/sobey/welcome.html']
    start_urls = ['http://https://www.smu.ca/academics/sobey/welcome.html/']

    def parse(self, response):
        pass
