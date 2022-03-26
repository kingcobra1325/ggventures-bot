import scrapy


class Ind0034Spider(scrapy.Spider):
    name = 'ind_0034'
    allowed_domains = ['https://collegedunia.com/college/28183-niilm-centre-for-management-studies-niilm-cms-greater-noida']
    start_urls = ['http://https://collegedunia.com/college/28183-niilm-centre-for-management-studies-niilm-cms-greater-noida/']

    def parse(self, response):
        pass
