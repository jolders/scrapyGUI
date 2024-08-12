from scrapy.loader import ItemLoader
from ..items import BooksScraperItem
from scrapy import Spider, Request


class BooksscraperSpider(Spider):
    name = "booksscraper"
    allowed_domains = ["books.toscrape.com"]
    #start_urls = ["https://books.toscrape.com/"]
    #start_urls = []


    def __init__(self, *args, **kwargs):
        super(BooksscraperSpider, self).__init__(*args, **kwargs)
        print(type(kwargs.get("start_urls")))
        print(kwargs.get("start_urls"))
        print(type(kwargs.get("pages")))
        print(kwargs.get("pages"))


        self.start_urls = kwargs.get("start_urls")
        print(f"START_URLS TYPE = :{type(self.start_urls)}")
        print(f"START_URLS = :{self.start_urls}")

        lis = kwargs.get("pages")
        res = [eval(i) for i in lis]
        print("RES", res)
        firstelement = res[0]

        self.page_count = 0
        self.max_pages = int(firstelement)
        print(f"firstelement: {firstelement}")

    def parse(self, response):
        self.page_count += 1
        #ebooks = response.css("article.product_pod")
        #loader = ItemLoader(item=BooksScraperItem())

        for ebook in response.css("article.product_pod"):
            #loader = ItemLoader(item=BooksScraperItem(), selector=ebook)
            #loader.add_css('title', 'h3 a::attr(title)')
            #loader.add_css('price', 'div.product_price p.price_color::text')
            #loader.add_css('URL', 'h3 a::attr(href)')
            #yield loader.load_item()
            url = ebook.css("h3 a").attrib["href"]
            yield Request(url=self.start_urls[0] + url, callback=self.parse_details)


        # NEXT PAGE LINK >
        next_page = response.css('li.next a::attr(href)').get()
        print(f"NEXTPAGE = :{next_page}")
        if next_page and self.page_count <= self.max_pages:
            next_page = response.urljoin(next_page)
            #next_page = f"{self.start_urls[0]}{next_btn.attrib['href']}"
            print(f"NEXTPAGE not none= :{next_page}")
            yield Request(next_page, callback=self.parse)

    def parse_details(self, response):
        # main = response.css("product_page")
        # initialize the itemloader with selector
        current_url = response.request.url
        # getend = current_url.re('?<=\/)[a-zA-Z0-9_-]+(?=\/index\.html')[0]
        # current_url = response.request.meta['redirect_urls']
        #redirect_urls = response.meta.get(r"redirect_urls")
        loader = ItemLoader(item=BooksScraperItem(), selector=response)
        loader.add_css("title", "div.product_main h1")
        loader.add_css("price", "div.product_main p.price_color")
        quantity_p = response.css("div.product_main p.availability")
        loader.add_value("quantity", quantity_p.re(r'\(.+ available\)')[0])
        # TABLE DATA
        loader.add_css("UPC", ".product_page table tr:nth-child(1) > td:nth-child(2)")
        loader.add_css("producttype", ".product_page table tr:nth-child(2) > td:nth-child(2)")
        loader.add_css("pricextax", ".product_page table tr:nth-child(3) > td:nth-child(2)")
        loader.add_css("availability", ".product_page table tr:nth-child(6) > td:nth-child(2)")
        loader.add_value("url", current_url)
        yield loader.load_item()