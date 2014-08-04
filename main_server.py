import urllib
from bs4 import BeautifulSoup
from tornado.io import IOLoop
from tornado.web import Application, RequestHandler

# Top traded symbols include: 
# BAC, SPY, IWM, EEM, AAPL, MSFT, TLT, DXJ, NS
# XLF, SLV, FB, QQQ, GPOR, XOP

TOP_SYMBOLS = ['BAC', 'SPY', 'IWM', 'EEM','AAPL', 'MSFT', 'TLT', 'DXJ', 'NS', 'XLF', 'SLV', 'FB', 'QQQ', 'GPOR', 'XOP']

class QuotesHandler(RequestHandler):
    def get_quotes(self)
        url = 'http://finance.yahoo.com/d/quotes.csv?s='
        for symbol in TOP_SYMBOLS:
            url += symbol + '+'
        url = url[:len(url) - 1]
        url += '&f=sn'

    def get(self, symbol):
        results = self.get_quotes()


settings = { 'static_path' : './static/' }

application([
    ('/(.*)', QuotesHandler)
    ], **settings)

if __name__ == '__main__':
    application.listen(8888)
    IOLoop.instance().start()
    
