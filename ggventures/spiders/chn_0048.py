import scrapy


class Chn0048Spider(scrapy.Spider):
    name = 'chn_0048'
    allowed_domains = ['https://www.university-directory.eu/China/Xian-Zhaohua-Administration-Education-Institute--Business-School.html']
    start_urls = ['http://https://www.university-directory.eu/China/Xian-Zhaohua-Administration-Education-Institute--Business-School.html/']

    def parse(self, response):
        pass
