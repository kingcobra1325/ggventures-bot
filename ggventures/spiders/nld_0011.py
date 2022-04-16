import scrapy


class Nld0011Spider(scrapy.Spider):
    name = 'nld_0011'
    allowed_domains = ['https://www.maastrichtuniversity.nl/about-um/faculties/school-business-and-economics']
    start_urls = ['http://https://www.maastrichtuniversity.nl/about-um/faculties/school-business-and-economics/']

    def parse(self, response):
        pass
