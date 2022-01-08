import scrapy


class Usa0076Spider(scrapy.Spider):
    name = 'usa_0076'
    allowed_domains = ['https://fisher.osu.edu/']
    start_urls = ['http://https://fisher.osu.edu//']

    def parse(self, response):
        pass
