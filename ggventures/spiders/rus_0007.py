import scrapy


class Rus0007Spider(scrapy.Spider):
    name = 'rus_0007'
    allowed_domains = ['https://eduniversal-ranking.com/business-school-university-ranking-in-russia/international-management-institute-link/profile-international-management-institute-link.html']
    start_urls = ['http://https://eduniversal-ranking.com/business-school-university-ranking-in-russia/international-management-institute-link/profile-international-management-institute-link.html/']

    def parse(self, response):
        pass
