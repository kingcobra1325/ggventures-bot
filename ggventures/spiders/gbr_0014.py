import scrapy


class Gbr0014Spider(scrapy.Spider):
    name = 'gbr_0014'
    allowed_domains = ['https://www.kingston.ac.uk/faculties/faculty-of-business-and-social-sciences/schools/kingston-business-school/']
    start_urls = ['http://https://www.kingston.ac.uk/faculties/faculty-of-business-and-social-sciences/schools/kingston-business-school//']

    def parse(self, response):
        pass
