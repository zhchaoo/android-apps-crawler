from scrapy.item import Item, Field

class AppItem(Item):
    app_name = Field()
    version = Field()
    url = Field()
