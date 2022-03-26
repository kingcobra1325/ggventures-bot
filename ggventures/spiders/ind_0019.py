import scrapy


class Ind0019Spider(scrapy.Spider):
    name = 'ind_0019'
    allowed_domains = ['https://home.iitd.ac.in/']
    start_urls = ['http://https://home.iitd.ac.in//']

    def parse(self, response):
        pass
