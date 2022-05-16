import scrapy


class Rus0018Spider(scrapy.Spider):
    name = 'rus_0018'
    allowed_domains = ['https://www.susu.ru/en/news/2021/01/11/opens-big-scale-professional-retraining-program']
    start_urls = ['http://https://www.susu.ru/en/news/2021/01/11/opens-big-scale-professional-retraining-program/']

    def parse(self, response):
        pass
