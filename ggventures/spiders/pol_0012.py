import scrapy


class Pol0012Spider(scrapy.Spider):
    name = 'pol_0012'
    allowed_domains = ['https://www.pw.edu.pl/engpw/Academics/WUT-Business-School']
    start_urls = ['http://https://www.pw.edu.pl/engpw/Academics/WUT-Business-School/']

    def parse(self, response):
        pass
