from abc import ABCMeta, abstractclassmethod
import requests
import datetime

class CoinnestClient():
    def __init__(self, credential):
        self.credential = credential

    def depth(market):
        params = {
            'coin': market.minor
        }
        r = requests.get("https://api.coinnest.co.kr/debth", params)
        resp = r.json()
        return {
            'ts': datatime.datetime.now().timestamp()
        }
