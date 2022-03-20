import scrapy


class Deu0007Spider(scrapy.Spider):
    name = 'deu_0007'
    allowed_domains = ['https://en.fh-muenster.de/msb/index.php']
    start_urls = ['http://https://en.fh-muenster.de/msb/index.php/']

    def parse(self, response):
        pass
