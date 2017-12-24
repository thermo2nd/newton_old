from pandas import DataFrame
import pandas as pd
import sqlalchemy as sa
from datetime import datetime, timedelta
from newton.db.config import engine

class CandleDao:
    @classmethod
    def query(_cls, duration=60, market='krw/btc',
    scope_from=datetime.now()-timedelta(minutes=60), scope_to=datetime.now()):
        with engine.connect() as conn, conn.begin():
            return pd.read_sql_query(sa.text("""
                    select time_bucket(':duration seconds', time) as timebucket, count(*)
                    as tick_cnt, max(bid) as bid_max,
                    min(bid) as bid_min, max(ask) as ask_max, min(ask) as
                    ask_min, max(last) as last_max, min(last) as last_min,
                    first(last, time) as open, last(last, time) as close 
                    from tickers where
                    market=:market and time between :scope_from and :scope_to group by
                    time order by time 
                    """), conn, params={'duration': duration, 'market': market,
                    'scope_from': scope_from, 'scope_to': scope_to})
