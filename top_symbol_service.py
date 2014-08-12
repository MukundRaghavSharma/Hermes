import json
import datetime
import urllib
from bs4 import BeautifulSoup
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler

# Top traded symbols include: 

TOP_SYMBOLS = ['BAC', 'SPY', 'IWM', 'EEM','AAPL', 'MSFT', 'TLT', 'DXJ', 'NS', 'XLF', 'SLV', 'FB', 'QQQ', 'GPOR', 'XOP']

DICTIONARY_LIST = ['Name', 'Bid', 'Ask']

class TopSymbolService:
    def __extract_data(self):
        url = 'http://finance.yahoo.com/d/quotes.csv?s='
        for symbol in TOP_SYMBOLS:
            url += symbol + '+'
        url = url[:len(url) - 1]
        url += '&f=snb2b3'
        raw = urllib.urlopen(url)
        soup = BeautifulSoup(raw)
        return soup 
    
    def get_quotes(self):
        soup = self.__extract_data()
        content = soup.findAll('body')[0].contents[0]
        split_strings = str(content).split('\n')
        results_list = []
        for string in split_strings:
            s = string.split(',')
            if len(s) == 4:# or len(s) == 5:
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
        self.render('front_end/index.html', results = results)

class HistoricalService(RequestHandler):
    def __extract_data(self, Symbol):
        url = 'http://real-chart.yahoo.com/table.csv?s=' 
        url += Symbol
        now = datetime.datetime.now().date()
        url += '&d='+ str(now.month) + '&e=' + str(now.day) + '&f=' + str(now.year)
        url += '&g=d'
        url += '&a=1&b=1&c=1900'
        url += '&ignore=.csv'
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
    
settings = { 'static_path' : './front_end/static/' }

application = Application([
    ('/topsymbols/', TopSymbolHandler),
    ('/historical/', HistoricalService)
    ], **settings)

if __name__ == '__main__':
    application.listen(8888)
    IOLoop.instance().start()
