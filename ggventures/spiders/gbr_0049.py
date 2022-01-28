import scrapy


class Gbr0049Spider(scrapy.Spider):
    name = 'gbr_0049'
    allowed_domains = ['https://www.cardiffmet.ac.uk/Pages/default.aspx']
    start_urls = ['http://https://www.cardiffmet.ac.uk/Pages/default.aspx/']

    def parse(self, response):
        pass
