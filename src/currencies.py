import urllib
from bs4 import BeautifulSoup

class Currencies:
    def __init__(self):
        self.currencies = {}
        url = "http://www.fxstreet.com/rates-charts/currency-rates/"
        raw = urllib.urlopen(url)
        soup = BeautifulSoup(raw)
        check = soup.findAll('tr')[1:33]
        for cp in check:
            count = 0
            currency = str(cp.findAll('td', {'class', 'col1'})[0].contents[0])
            if currency not in self.currencies.keys():
                self.currencies[currency] = {} 
            for val in cp.findAll('td'):
                if count == 0:
                    count += 1
                    continue
                s = val['id']
                new_s = str(s.split('_')[0])
                if ':' not in val.contents[0]:
                    val.contents[0] = float(val.contents[0])
                else:
                    val.contents[0] = str(val.contents[0])
                self.currencies[currency][new_s] = val.contents[0]

if __name__ == '__main__':
    c = Currencies()
    print c.currencies
