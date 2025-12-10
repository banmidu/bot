# SampleStrategy for Freqtrade
from freqtrade.strategy import IStrategy

class SampleStrategy(IStrategy):
    timeframe = '5m'

    def populate_indicators(self, dataframe, metadata):
        return dataframe

    def populate_buy_trend(self, dataframe, metadata):
        dataframe['buy'] = 0
        return dataframe

    def populate_sell_trend(self, dataframe, metadata):
        dataframe['sell'] = 0
        return dataframe
