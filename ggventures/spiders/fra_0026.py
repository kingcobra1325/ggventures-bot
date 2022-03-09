import scrapy


class Fra0026Spider(scrapy.Spider):
    name = 'fra_0026'
    allowed_domains = ['https://en.grenoble-em.com/']
    start_urls = ['http://https://en.grenoble-em.com//']

    def parse(self, response):
        pass
