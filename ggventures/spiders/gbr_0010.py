import scrapy


class Gbr0010Spider(scrapy.Spider):
    name = 'gbr_0010'
    allowed_domains = ['https://www.dmu.ac.uk/schools-departments/lcbs/about.aspx']
    start_urls = ['http://https://www.dmu.ac.uk/schools-departments/lcbs/about.aspx/']

    def parse(self, response):
        pass
