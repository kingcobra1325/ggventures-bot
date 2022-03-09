import scrapy


class Fra0046Spider(scrapy.Spider):
    name = 'fra_0046'
    allowed_domains = ['https://www.topuniversities.com/universities/esa-ecole-superieure-des-affaires']
    start_urls = ['http://https://www.topuniversities.com/universities/esa-ecole-superieure-des-affaires/']

    def parse(self, response):
        pass
