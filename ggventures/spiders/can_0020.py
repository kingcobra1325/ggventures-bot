import scrapy


class Can0020Spider(scrapy.Spider):
    name = 'can_0020'
    allowed_domains = ['https://telfer.uottawa.ca/en/']
    start_urls = ['http://https://telfer.uottawa.ca/en//']

    def parse(self, response):
        pass
