import json
import urllib
from bs4 import BeautifulSoup
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler

# Top traded symbols include: 

TOP_SYMBOLS = ['BAC', 'SPY', 'IWM', 'EEM','AAPL', 'MSFT', 'TLT', 'DXJ', 'NS', 'XLF', 'SLV', 'FB', 'QQQ', 'GPOR', 'XOP']

class TopSymbolService:
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
        print json.dumps(results)
        return json.dumps(results)   

class TopSymbolHandler(RequestHandler):
    service = TopSymbolService()
    
    def get(self):
        results = self.service.get_quotes()
        result_keys = results.keys()
        self.render('index.html', result_keys=result_keys)

settings = { 'static_path' : './static/' }

application = Application([
    ('/top_symbols/', TopSymbolHandler)
    ], **settings)

if __name__ == '__main__':
    application.listen(8888)
    IOLoop.instance().start()
    
