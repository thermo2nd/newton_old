from newton.db.seed import CandleSticks
from newton.dao.base import DaoBase

class CandleSticksDao(DaoBase):

    @classmethod
    def query(_cls, duration=60, major='krw', minor='btc',
    scope_from=datetime.now()-timedelta(minutes=60), scope_to=datetime.now()):
        with engine.connect() as conn, conn.begin():
            return pd.read_sql_query(sa.text("""
                    select time_bucket(':duration seconds', time) as timebucket,
                    :duration as duration, major, minor, 
                    first(open, time) as open, last(close, time) as close ,
                    max(high) as high, min(low) as low, SUM(volume) as volume
                    from tickers where
                    major =:major and minor = :minor and time
                    between :scope_from and :scope_to
                    group by timebucket order by timebucket 
                    """), conn, params={'duration': duration, 'major': major,
                    'minor':minor, 'scope_from': scope_from, 'scope_to': scope_to})
