from abc import ABCMeta, abstractmethod
from contextlib import contextmanager
import numbers
from sqlalchemy.exc import SQLAlchemyError

from newton.db.config import Session
from newton.logger import bot_logger


class DaoBase(metaclass=ABCMeta):

    @staticmethod
    @contextmanager
    def _transaction():
        s = Session()
        try:
            yield s
            s.commit()
        except SQLAlchemyError as e:
            bot_logger.exception(e)
            s.rollback()
            raise
        finally:
            s.close()

    @staticmethod
    @contextmanager
    def _session():
        s = Session()
        try:
            yield s
        except SQLAlchemyError as e:
            bot_logger.exception(e)
            raise
        finally:
            s.close()

    @classmethod
    def save(cls, item):
        with cls._session() as s:
            s.add(item)
            s.commit()
            s.refresh(item)
            return item

    @classmethod
    def save_list(cls, items):
        with cls._session() as s:
            for item in items:
                s.add(item)
            s.commit()
