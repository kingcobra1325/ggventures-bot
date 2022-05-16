import scrapy


class Rus0019Spider(scrapy.Spider):
    name = 'rus_0019'
    allowed_domains = ['https://www.masterstudies.com/universities/Russia/VSUES/']
    start_urls = ['http://https://www.masterstudies.com/universities/Russia/VSUES//']

    def parse(self, response):
        pass
