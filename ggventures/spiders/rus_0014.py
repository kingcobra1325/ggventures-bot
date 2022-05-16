import scrapy


class Rus0014Spider(scrapy.Spider):
    name = 'rus_0014'
    allowed_domains = ['https://www.rea.ru/en/org/faculties/Pages/ibs.aspx']
    start_urls = ['http://https://www.rea.ru/en/org/faculties/Pages/ibs.aspx/']

    def parse(self, response):
        pass
