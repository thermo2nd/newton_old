from abc import ABCMeta, abstractclassmethod
import requests
import datetime
from newton.db.dao.tickers import TickersDao
from newton.db.seed import Tickers

class Client(metaclass=ABCMeta):
    def __str__(self):
        return self.name

class CoinnestClient():
    def __init__(self, credential):
        self.credential = credential
        self.name = 'coinnest'

    def ticker(self, market):
        params = {
            'coin': market.minor
        }
        r = requests.get("https://api.coinnest.co.kr/api/pub/ticker", params)
        resp = r.json()
        ticker = Tickers(market = market, bid=resp['buy'], ask=resp['sell'],
        last=resp['last'], svr_time=resp['time'])
        TickersDao.save(ticker)
        return {
            'ts': datetime.datetime.now().timestamp(),
            'svr_ts': resp['time'],
            'bid': resp['buy'],
            'ask': resp['sell'],
            'last': resp['last']
        }
