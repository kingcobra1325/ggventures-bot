import scrapy


class Fra0044Spider(scrapy.Spider):
    name = 'fra_0044'
    allowed_domains = ['https://iae.univ-lyon3.fr/accueil-en']
    start_urls = ['http://https://iae.univ-lyon3.fr/accueil-en/']

    def parse(self, response):
        pass
