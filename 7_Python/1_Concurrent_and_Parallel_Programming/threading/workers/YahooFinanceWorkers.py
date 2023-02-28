import threading
import requests
from bs4 import BeautifulSoup
from lxml import html
import time
import random

class YahooFinancepriceWorker(threading.Thread):

    def __init__(self, symbol, **kwargs):
        super(YahooFinancepriceWorker, self).__init__(**kwargs)
        self._symbol = symbol
        base_url = 'https://finance.yahoo.com/quote/'
        self._url = f'{base_url}{self._symbol}'
        self.start()

    def run(self):
        # Every thread sleeps in between 0-20 s randomly
        time.sleep(5*random.random())
        r = requests.get(self._url)
        if r.status_code != 200:
            print("Could not get entries in YahooFinanceWorkers!")
            return
        page_contents = html.fromstring(r.text)
        raw_price = page_contents.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]')[0].text
        price = float(raw_price.replace(',', ''))
        print("Stock: ", self._symbol, " and Price: ", price)
        return price


