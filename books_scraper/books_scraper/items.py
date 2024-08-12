from scrapy import Item, Field
import re
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

def get_price(txt):
    return float(txt.replace('£', ''))

def get_quantity(txt):
    # takes txt as '(19 available)' pattern
    # and returns 19 from the pattern
    return int(txt.replace('(', '').split()[0])

def use_regex(input_text):
    pattern = r"(?<=\/)[a-zA-Z0-9_-]+(?=\/index\.html)"
    match = re.search(pattern, input_text).group()
    myurl = f"https://books.toscrape.com/catalogue/" + match + "/index.html"
    return myurl

class BooksScraperItem(Item):
    title = Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    price = Field(input_processor=MapCompose(remove_tags, get_price), output_processor=TakeFirst())
    quantity = Field(input_processor=MapCompose(get_quantity), output_processor=TakeFirst())
    UPC = Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    producttype = Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    pricextax = Field(input_processor=MapCompose(remove_tags, get_price), output_processor=TakeFirst())
    availability = Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    url = Field(input_processor=MapCompose(use_regex), output_processor=TakeFirst())

    #URL = Field(input_processor=MapCompose(use_regex), output_processor=TakeFirst())
