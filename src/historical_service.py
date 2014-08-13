import datetime
import urllib
import os
import sys

from bs4 import BeautifulSoup
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
from dictionary_parser import parse_dictionary

SYMBOL = 'GOOG'

ATTRIBUTES_LIST = ['Symbol', 'Name', 'Open',
                   'High'  , 'Low' , 'Close', 'Volume', 'Adjusted Close']

class HistoricalService(RequestHandler):
    def __extract_data(self, Symbol):
        url = 'http://real-chart.yahoo.com/table.csv?s=' 
        url += SYMBOL
        now = datetime.datetime.now().date()
        url += '&d='+ str(now.month) + '&e=' + str(now.day) + '&f=' + str(now.year)
        url += '&g=d'
        url += '&a=1&b=1&c=1900'
        url += '&ignore=.csv'
        print url
        raw = urllib.urlopen(url)
        soup = BeautifulSoup(raw)
        return soup

    def get_data(self):
        goog = self.__extract_data('GOOG')
        content = goog.findAll('body').contents[0]
        print content
        return content 

    def get(self):
        print self.get_data()
        self.write(self.get_data())

application = Application([
    ('/historical/GOOG/', HistoricalService),
    ])

if __name__ == '__main__':
    application.listen(8889)
    IOLoop.instance().start()
