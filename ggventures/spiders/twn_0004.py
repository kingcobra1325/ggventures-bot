import scrapy


class Twn0004Spider(scrapy.Spider):
    name = 'twn_0004'
    allowed_domains = ['https://www.com.nctu.edu.tw/index.php?lang=en']
    start_urls = ['http://https://www.com.nctu.edu.tw/index.php?lang=en/']

    def parse(self, response):
        pass
