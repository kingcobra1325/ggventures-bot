# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


class GgventuresItem(scrapy.Item):
    """
    Sets the fields required for the data to be scraped
    for each event
    """
    # university_name = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    university_name = scrapy.Field()
    university_contact_info = scrapy.Field()
    logo = scrapy.Field()
    event_name = scrapy.Field()
    event_date = scrapy.Field()
    event_time = scrapy.Field()
    event_link = scrapy.Field()
    event_desc = scrapy.Field()
    startups_name = scrapy.Field()
    startups_link = scrapy.Field()
    startups_contact_info = scrapy.Field()
