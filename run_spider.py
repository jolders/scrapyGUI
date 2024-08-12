from scrapy.settings import Settings

# import main
from books_scraper.books_scraper import settings as my_settings
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from books_scraper.books_scraper.spiders.booksscraper import BooksscraperSpider
import sys
# from scrapy.utils.project import get_project_settings

# pip install scrapy
# scrapy startproject books_scraper
# cd books_scraper
# scrapy genspider booksscraper https://example.co.uk

# make changes to Pipelines.py
# SPIDER_MODULES = ["books_scraper.books_scraper.spiders"]
# NEWSPIDER_MODULE = "books_scraper.books_scraper.spiders"
# ITEM_PIPELINES = {"books_scraper.books_scraper.pipelines.BooksScraperPipeline": 300,}


def run(urlselected, spinboxvalue):
    urlselected = sys.argv[1]
    spinboxvalue = sys.argv[2]
    # Set a reference to the window in the spider
    #BooksscraperSpider.window = window
    print(f"PRINTING THE VALUE :{urlselected}")
    print(f"PRINTING THE VALUE :{spinboxvalue}")
    #print(f"PRINTING THE VALUE : {strb}")
    crawler_settings = Settings()
    crawler_settings.setmodule(my_settings)
    process = CrawlerProcess(settings=crawler_settings)
    #process = CrawlerProcess(get_project_settings())
    process.crawl(BooksscraperSpider, start_urls=[f"{urlselected}"], pages=[f"{spinboxvalue}"])
    process.start()

if __name__ == '__main__':
    run(str, str)