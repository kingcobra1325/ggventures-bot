import scrapy


class Fra0051Spider(scrapy.Spider):
    name = 'fra_0051'
    allowed_domains = ['https://tsm-education.fr/en']
    start_urls = ['http://https://tsm-education.fr/en/']

    def parse(self, response):
        pass
