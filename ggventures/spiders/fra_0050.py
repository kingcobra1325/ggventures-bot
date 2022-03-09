import scrapy


class Fra0050Spider(scrapy.Spider):
    name = 'fra_0050'
    allowed_domains = ['https://www.kcl.ac.uk/study-legacy/abroad/discover/destinations/exchange-partners/europe/universite-de-strasbourg-robert-schuman']
    start_urls = ['http://https://www.kcl.ac.uk/study-legacy/abroad/discover/destinations/exchange-partners/europe/universite-de-strasbourg-robert-schuman/']

    def parse(self, response):
        pass
