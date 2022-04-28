import scrapy


class Col0003Spider(scrapy.Spider):
    name = 'col_0003'
    allowed_domains = ['https://uniandes.edu.co/en']
    start_urls = ['http://https://uniandes.edu.co/en/']

    def parse(self, response):
        pass
