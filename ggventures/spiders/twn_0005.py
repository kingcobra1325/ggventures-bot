import scrapy


class Twn0005Spider(scrapy.Spider):
    name = 'twn_0005'
    allowed_domains = ['https://www.cm.nsysu.edu.tw/?Lang=en']
    start_urls = ['http://https://www.cm.nsysu.edu.tw/?Lang=en/']

    def parse(self, response):
        pass
