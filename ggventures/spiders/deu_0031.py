import scrapy


class Deu0031Spider(scrapy.Spider):
    name = 'deu_0031'
    allowed_domains = ['https://www.uni-regensburg.de/business-economics-and-management-information-systems/faculty/index.html#:~:text=The%20Faculty%20of%20Business%2C%20Economics,recognized%20for%20its%20practical%20application.']
    start_urls = ['http://https://www.uni-regensburg.de/business-economics-and-management-information-systems/faculty/index.html#:~:text=The%20Faculty%20of%20Business%2C%20Economics,recognized%20for%20its%20practical%20application./']

    def parse(self, response):
        pass
