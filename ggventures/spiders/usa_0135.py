import scrapy


class Usa0135Spider(scrapy.Spider):
    name = 'usa_0135'
    allowed_domains = ['https://sc.edu/study/colleges_schools/moore/index.php']
    start_urls = ['http://https://sc.edu/study/colleges_schools/moore/index.php/']

    def parse(self, response):
        pass
