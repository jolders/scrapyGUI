import os
import sqlite3

from sqlConnection import Data


class BooksScraperPipeline:
    def __init__(self):
        print("---o----<<[ INITIATING PIPELINES ]>>----o----\n")
        #self.con = sqlite3.connect('books.db')
        #self.cur = self.con.cursor()

    def process_item(self, item, spider):
        print(f"PIPELINE TITLE : {item['title']}")
        print(f"PIPELINE URL : {item['price']}")
        print(f"PIPELINE URL : {item['quantity']}")
        print(f"PIPELINE URL : {item['UPC']}")
        print(f"PIPELINE URL : {item['producttype']}")
        print(f"PIPELINE URL : {item['pricextax']}")
        print(f"PIPELINE URL : {item['availability']}")
        print(f"PIPELINE URL : {item['url']}")


        # PASS DATA TO SQL FOR PROCESSING
        try:
            with sqlite3.connect('books.db') as self.con:
                self.cur = self.con.cursor()
                self.cur.execute('INSERT INTO booksdb (Title, Price, Quantity, UPC, Product, Availability, URL) VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (item['title'], item['price'], item['quantity'], item['UPC'], item['producttype'], item['availability'],item['url']))
        except sqlite3.Error as er:
            print(f"Database insert error: {er}")

        return item

    def close_spider(self, spider):
        self.con.commit()
