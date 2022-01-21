import scrapy


class Gbr0019Spider(scrapy.Spider):
    name = 'gbr_0019'
    allowed_domains = ['https://www.alliancembs.manchester.ac.uk/']
    start_urls = ['http://https://www.alliancembs.manchester.ac.uk//']

    def parse(self, response):
        pass
