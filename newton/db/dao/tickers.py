from .base import DaoBase


class TickersDao(DaoBase):
    def __init__(self, market):
        super().__init__()
        self._market = str(market)

    def _get_model(self):
        return None 

    @classmethod
    def save(cls, arr):
        with cls._session() as s:
            s.execute("""INSERT INTO tickers2 (time, market, price, quantity)
            values (:time, :market, :price, :quantity)""", arr)

    @classmethod
    def get_latest(cls):
        with cls._session() as s:
            result = s.execute("""
            SELECT market, max(time) as latest from tickers2 GROUP BY market"""
            ).fetchall()
            return result 
