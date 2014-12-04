from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
from src.top_symbol_service import TopSymbolHandler
from src.historical_service import HistoricalHandler

if __name__ == '__main__':

    settings = { 'static_path' : 'front_end/static' }
    application = Application([
        ('/topsymbols', TopSymbolHandler),
        (r'/historical/(.*)', HistoricalHandler),
    ], **settings)
    application.listen(8888)
    IOLoop.instance().start()
