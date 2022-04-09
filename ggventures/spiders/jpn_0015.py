import scrapy


class Jpn0015Spider(scrapy.Spider):
    name = 'jpn_0015'
    allowed_domains = ['https://admissions.apu.ac.jp/graduate/academics/']
    start_urls = ['http://https://admissions.apu.ac.jp/graduate/academics//']

    def parse(self, response):
        pass
