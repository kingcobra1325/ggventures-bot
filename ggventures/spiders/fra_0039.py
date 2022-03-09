import scrapy


class Fra0039Spider(scrapy.Spider):
    name = 'fra_0039'
    allowed_domains = ['https://iae-aix.univ-amu.fr/en/home']
    start_urls = ['http://https://iae-aix.univ-amu.fr/en/home/']

    def parse(self, response):
        pass
