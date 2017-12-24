from talib import abstract
from pandas import DataFrame
import pandas as pd

class Indicator():

    @classmethod
    def add_rsi(_cls, data, period=14):
        rsi_series = abstract.Function('rsi')(data, price='close',
        timeperiod=period)
        rsi_series.rename("rsi"+str(period), inplace=True)
        data_rsi_added = pd.concat([data, rsi_series], axis=1)
        data_rsi_added.dropna(inplace=True)
        dict_data_rsi_added = data_rsi_added.astype(object).to_dict(orient='records')
        return data_rsi_added

    @classmethod
    def add_ma(_cls, data, period=50):
        series = abstract.Function('ma')(data, price='close',
        timeperiod=period)
        series.rename("ma"+str(period), inplace=True)
        data_added = pd.concat([data, series], axis=1)
        data_added.dropna(inplace=True)
        dict_data_added = data_added.astype(object).to_dict(orient='records')
        return data_added
