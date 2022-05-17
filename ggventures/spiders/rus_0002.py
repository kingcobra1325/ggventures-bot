import scrapy


class Rus0002Spider(scrapy.Spider):
    name = 'rus_0002'
    allowed_domains = ['https://www.eduniversal-ranking.com/business-school-university-ranking-in-russia/higher-commercial-management-school-hcms-of-the-russian-foreign-trade-academy-of-the-ministry-for-economic-development-of-russia-rfta.html']
    start_urls = ['http://https://www.eduniversal-ranking.com/business-school-university-ranking-in-russia/higher-commercial-management-school-hcms-of-the-russian-foreign-trade-academy-of-the-ministry-for-economic-development-of-russia-rfta.html/']

    def parse(self, response):
        pass
