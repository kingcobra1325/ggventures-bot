import scrapy


class Kor0002Spider(scrapy.Spider):
    name = 'kor_0002'
    allowed_domains = ['https://eduniversal-ranking.com/business-school-university-ranking-in-south-korea/chonnam-national-university-college-of-business-administration/profile-chonnam-national-university-college-of-business-administration.html']
    start_urls = ['http://https://eduniversal-ranking.com/business-school-university-ranking-in-south-korea/chonnam-national-university-college-of-business-administration/profile-chonnam-national-university-college-of-business-administration.html/']

    def parse(self, response):
        pass
