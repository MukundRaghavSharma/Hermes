import json
import datetime
import urllib
import os
import sys

sys.path.append('../')

from bs4 import BeautifulSoup
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
from dictionary_parser import parse_dictionary


# Top traded symbols include: 
TOP_SYMBOLS = ['BAC', 'SPY', 'IWM', 'EEM','AAPL', 'MSFT', 'TLT', 'DXJ', 'NS', 'XLF', 'SLV', 'FB', 'QQQ', 'GPOR', 'XOP']

# Attributes
ATTRIBUTES_LIST = ['Symbol', 'Name', 'Bid-Realtime', 'Ask-Realtime' ]

class TopSymbolService:
    def __extract_data(self):
        url = 'http://finance.yahoo.com/d/quotes.csv?s='
        for symbol in TOP_SYMBOLS:
            url += symbol + '+'
        attributes_result = parse_dictionary(ATTRIBUTES_LIST)
        url = url[:len(url) - 1]
        url += '&f=' 
        for attributes in attributes_result:
            url += str(attributes)
        url += '&ignore=.csv'
        raw = urllib.urlopen(url)
        soup = BeautifulSoup(raw)
        return soup 
    
    def get_quotes(self):
        soup = self.__extract_data()
        content = soup.findAll('body')[0].contents[0]
        split_strings = str(content).split('\n')
        results_list = []
        for string in split_strings:
            if len(string) < 1:
                continue
            s = string.split(',')
            if len(s) >= len(ATTRIBUTES_LIST):        
                individual_list = []
                individual_list.append(s[0].replace('"',''))
                for a in s[1:]:
                    individual_list.append(a)
                results_list.append(individual_list)
        return results_list

class TopSymbolHandler(RequestHandler):
    service = TopSymbolService()
    
    def get(self):
        results = self.service.get_quotes()
        self.render('../front_end/index.html', results = results)

    
settings = { 'static_path' : '../front_end/static/' }

application = Application([
    ('/topsymbols/', TopSymbolHandler),
    ], **settings)

if __name__ == '__main__':
    application.listen(8888)
    IOLoop.instance().start()
