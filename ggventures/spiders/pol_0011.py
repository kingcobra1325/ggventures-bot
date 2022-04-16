import scrapy


class Pol0011Spider(scrapy.Spider):
    name = 'pol_0011'
    allowed_domains = ['https://www.unipage.net/en/7399/gda_sk_management_college']
    start_urls = ['http://https://www.unipage.net/en/7399/gda_sk_management_college/']

    def parse(self, response):
        pass
