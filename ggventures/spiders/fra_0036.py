import scrapy


class Fra0036Spider(scrapy.Spider):
    name = 'fra_0036'
    allowed_domains = ['https://www.sciencespo.fr/en']
    start_urls = ['http://https://www.sciencespo.fr/en/']

    def parse(self, response):
        pass
