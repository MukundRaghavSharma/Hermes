import json
import urllib
from bs4 import BeautifulSoup
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler

# Top traded symbols include: 

TOP_SYMBOLS = ['BAC', 'SPY', 'IWM', 'EEM','AAPL', 'MSFT', 'TLT', 'DXJ', 'NS', 'XLF', 'SLV', 'FB', 'QQQ', 'GPOR', 'XOP']

DICTIONARY_LIST = ['Name', 'Bid', 'Ask']


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
            print len(s)
            if len(s) == 4 or len(s) == 5:
                individual_results = {}
                individual_results['Name'] = s[1]
                print s[1]
                individual_results['Ask'] = s[2]
                individual_results['Bid'] = s[3]
                results[s[0]] = individual_results
        return results

class TopSymbolHandler(RequestHandler):
    service = TopSymbolService()
    
    def get(self):
        results = self.service.get_quotes()
        self.write(results)

settings = { 'static_path' : './static/' }

application = Application([
    ('/top_symbols/', TopSymbolHandler)
    ], **settings)

if __name__ == '__main__':
    application.listen(8888)
    IOLoop.instance().start()
    
