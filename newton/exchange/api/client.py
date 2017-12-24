from abc import ABCMeta, abstractclassmethod
import requests
import datetime

_RETRY_COUNT = 5
_WAIT_SECOND = 5

def _with_retry(func):
    def _wrapper(self, *args, **kwargs):
        for i in range(_RETRY_COUNT):
            try:
                return func(self, *args, **kwargs)
            except Exception as e:
                a = random.uniform(0.1, 0.5)
                time.sleep(a)
                if i >= _RETRY_COUNT - 1:
                    raise e
                continue
    return _wrapper

class CoinoneClient():
    def __init__(self, credential):
        self.credential = credential
        self.name = 'coinone'

    @_with_retry
    def transactions(self, market):
        params = {
            'currency': market.minor,
            'period': 'hour'
        }

        r = requests.get("https://api.coinone.co.kr/trades/", params)
        resp = r.json()
        if resp['errorCode'] != '0':
            raise Exception("coinone api error")

        return resp['completeOrders']
