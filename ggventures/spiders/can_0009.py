import scrapy


class Can0009Spider(scrapy.Spider):
    name = 'can_0009'
    allowed_domains = ['https://smith.queensu.ca/index.php']
    start_urls = ['http://https://smith.queensu.ca/index.php/']

    def parse(self, response):
        pass
