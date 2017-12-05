from newton.local_settings import DATABASE as db
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


def __db_path():
    return 'postgresql://{0}:{1}@{2}/{3}'.format(db['USER'], db['PASSWORD'],
    db['URL'],
    db['DB'])


def _get_engine(file_path):
    my_engine = None

    def _create_engine():
        nonlocal my_engine
        if my_engine:
            return my_engine
        my_engine = create_engine(file_path, isolation_level="AUTOCOMMIT")
        return my_engine
    my_engine = _create_engine()
    return my_engine


engine = _get_engine(__db_path())
metadata = MetaData(bind=engine)
Session = sessionmaker(bind=engine)
Base = declarative_base(metadata=metadata)
