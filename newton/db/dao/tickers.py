from newton.db.seed import Tickers
from .base import DaoBase


class TickersDao(DaoBase):
    def __init__(self, market):
        super().__init__()
        self._market = str(market)

    def _get_model(self):
        return Tickers 

    @classmethod
    def save(cls, item):
        print(item)
        with cls._session() as s:
            s.execute("""INSERT INTO tickers (time, market, ask, bid, last) values (now(), :market, :ask, :bid, :last)""", 
            {
                "market": str(item.market),
                "ask": item.ask,
                "bid": item.bid,
                "last": item.last
            })
            return item
