import scrapy


class Zaf0015Spider(scrapy.Spider):
    name = 'zaf_0015'
    allowed_domains = ['https://www.ul.ac.za/tgsl/index.php?Entity=About%20TGSL']
    start_urls = ['http://https://www.ul.ac.za/tgsl/index.php?Entity=About%20TGSL/']

    def parse(self, response):
        pass
