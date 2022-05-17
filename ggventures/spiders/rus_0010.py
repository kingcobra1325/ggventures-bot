import scrapy


class Rus0010Spider(scrapy.Spider):
    name = 'rus_0010'
    allowed_domains = ['https://www.best-masters.com/master-at-higher-economic-school-of-saintpetersburg-state-university-of-economics-and-finance-hes-spbsuef.html']
    start_urls = ['http://https://www.best-masters.com/master-at-higher-economic-school-of-saintpetersburg-state-university-of-economics-and-finance-hes-spbsuef.html/']

    def parse(self, response):
        pass
