import scrapy


class Deu0006Spider(scrapy.Spider):
    name = 'deu_0006'
    allowed_domains = ['https://www.bwl.hm.edu/english_version/department_1/aboutus_2/aboutus.en.html']
    start_urls = ['http://https://www.bwl.hm.edu/english_version/department_1/aboutus_2/aboutus.en.html/']

    def parse(self, response):
        pass
