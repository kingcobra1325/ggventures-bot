import scrapy


class Ind0029Spider(scrapy.Spider):
    name = 'ind_0029'
    allowed_domains = ['https://en.wikipedia.org/wiki/Premiership_of_Lal_Bahadur_Shastri']
    start_urls = ['http://https://en.wikipedia.org/wiki/Premiership_of_Lal_Bahadur_Shastri/']

    def parse(self, response):
        pass
