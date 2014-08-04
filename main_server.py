import json
import urllib
from bs4 import BeautifulSoup
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler

# Top traded symbols include: 

TOP_SYMBOLS = ['BAC', 'SPY', 'IWM', 'EEM','AAPL', 'MSFT', 'TLT', 'DXJ', 'NS', 'XLF', 'SLV', 'FB', 'QQQ', 'GPOR', 'XOP']

class TopSymbolHandler(RequestHandler):
    def get_quotes(self):
        url = 'http://finance.yahoo.com/d/quotes.csv?s='
        for symbol in TOP_SYMBOLS:
            url += symbol + '+'
        url = url[:len(url) - 1]
        url += '&f=snab'
        raw = urllib.urlopen(url)
        soup = BeautifulSoup(raw)
        content = soup.findAll('body')[0].contents[0]
        split_strings = str(content).split('\n')
        results = {}
        for string in split_strings:
            s = string.split(',')
            results[s[0]] = s[1:]
        for key in results:


    def get(self):
        results = self.get_quotes()
        self.render('search.html', results=results)

settings = { 'static_path' : './static/' }

application = Application([
    ('/top_symbols/', TopSymbolHandler)
    ], **settings)

if __name__ == '__main__':
    application.listen(8888)
    IOLoop.instance().start()
    
