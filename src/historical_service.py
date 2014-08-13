import datetime
import urllib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  

from bs4 import BeautifulSoup
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
from util.dictionary_parser import parse_dictionary

class HistoricalHandler(RequestHandler):
    def __extract_data(self, symbol):
        url = 'http://real-chart.finance.yahoo.com/table.csv?s=' 
        url += symbol
        now = datetime.datetime.now().date()
        url += '&d='+ str(now.month) + '&e=' + str(now.day) + '&f=' + str(now.year)
        url += '&g=d'
        url += '&a=1&b=1&c=1900'
        url += '&ignore=.csv'
        raw = urllib.urlopen(url)
        soup = BeautifulSoup(raw)
        return soup

    def get_data(self, symbol):
        goog = self.__extract_data(symbol)
        check = goog.find('p', {'class':'more'})
        if check != None and str(check.contents[0]) == 'Please try ':
            return None
        content = goog.findAll('body')[0].contents[0]
        split_strings = str(content).split('\n')
        results_list = []
        first = True
        for string in split_strings:
            if len(string) < 1 or first:
                first = False
                continue
            s = string.split(',')
            individual_list = []
            individual_list.append(s[0])
            for a in s[1:]:
                individual_list.append(a)
            results_list.append(individual_list)
        return results_list

    def get(self, symbol):
        url = 'http://finance.yahoo.com/d/quotes.csv?s=' + symbol + '&f=n&ignore=.csv'
        raw = urllib.urlopen(str(url))
        soup = BeautifulSoup(raw)
        results = self.get_data(symbol)
        if results == None:
            self.render(os.path.join(os.getcwd(), 'front_end/error.html'))
        else:
            name = soup.findAll('body')[0].contents[0]
            name = name.replace('"', '')
            self.render(os.path.join(os.getcwd(), 'front_end/historical.html'), results = results, name = name)
