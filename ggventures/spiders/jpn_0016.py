import scrapy


class Jpn0016Spider(scrapy.Spider):
    name = 'jpn_0016'
    allowed_domains = ['https://www.u-tokyo.ac.jp/en/academics/facultyofeconomics.html']
    start_urls = ['http://https://www.u-tokyo.ac.jp/en/academics/facultyofeconomics.html/']

    def parse(self, response):
        pass
