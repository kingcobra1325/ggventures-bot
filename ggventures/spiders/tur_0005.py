import scrapy


class Tur0005Spider(scrapy.Spider):
    name = 'tur_0005'
    allowed_domains = ['https://isletme.istanbul.edu.tr/en/content/our-faculty/the-mission-and-vision-of-the-school']
    start_urls = ['http://https://isletme.istanbul.edu.tr/en/content/our-faculty/the-mission-and-vision-of-the-school/']

    def parse(self, response):
        pass
