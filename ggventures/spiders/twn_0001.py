import scrapy


class Twn0001Spider(scrapy.Spider):
    name = 'twn_0001'
    allowed_domains = ['http://www.management.fju.edu.tw/index_en.php']
    start_urls = ['http://http://www.management.fju.edu.tw/index_en.php/']

    def parse(self, response):
        pass
