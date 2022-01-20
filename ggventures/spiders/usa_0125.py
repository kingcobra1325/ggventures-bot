import scrapy


class Usa0125Spider(scrapy.Spider):
    name = 'usa_0125'
    allowed_domains = ['https://www.unk.edu/academics/bt/index.php']
    start_urls = ['http://https://www.unk.edu/academics/bt/index.php/']

    def parse(self, response):
        pass
