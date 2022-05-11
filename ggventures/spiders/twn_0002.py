import scrapy


class Twn0002Spider(scrapy.Spider):
    name = 'twn_0002'
    allowed_domains = ['https://researchoutput.ncku.edu.tw/en/organisations/college-of-management']
    start_urls = ['http://https://researchoutput.ncku.edu.tw/en/organisations/college-of-management/']

    def parse(self, response):
        pass
