import scrapy


class Rus0005Spider(scrapy.Spider):
    name = 'rus_0005'
    allowed_domains = ['https://eduniversal-ranking.com/business-school-university-ranking-in-russia/sinerghia-institute-of-economics-and-finance.html']
    start_urls = ['http://https://eduniversal-ranking.com/business-school-university-ranking-in-russia/sinerghia-institute-of-economics-and-finance.html/']

    def parse(self, response):
        pass
