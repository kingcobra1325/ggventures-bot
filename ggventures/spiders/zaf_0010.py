import scrapy


class Zaf0010Spider(scrapy.Spider):
    name = 'zaf_0010'
    allowed_domains = ['https://www.ru.ac.za/businessschool/about/history/']
    start_urls = ['http://https://www.ru.ac.za/businessschool/about/history//']

    def parse(self, response):
        pass
