import pandas as pd
import numpy as np
import talib

class StrategyEngine:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.signals = pd.DataFrame(index=data.index)

    def apply_momentum_strategy(self):
        """
        Example Strategy: Momentum Breakout
        Uses VWAP, RSI, and EMA crossover.
        """
        # Ensure we have required columns
        if not all(col in self.data.columns for col in ['close', 'high', 'low', 'volume']):
            raise ValueError("Missing required columns in data")

        close = self.data['close'].values

        # Calculate Indicators
        self.data['RSI'] = talib.RSI(close, timeperiod=14)
        self.data['EMA9'] = talib.EMA(close, timeperiod=9)
        self.data['EMA21'] = talib.EMA(close, timeperiod=21)

        # Simple VWAP calculation
        typical_price = (self.data['high'] + self.data['low'] + self.data['close']) / 3
        self.data['VWAP'] = (typical_price * self.data['volume']).cumsum() / self.data['volume'].cumsum()

        # Generate Signals
        # Long Entry: EMA9 > EMA21 AND Close > VWAP AND RSI > 60
        self.signals['long_entry'] = (
            (self.data['EMA9'] > self.data['EMA21']) &
            (self.data['close'] > self.data['VWAP']) &
            (self.data['RSI'] > 60)
        )

        # Short Entry: EMA9 < EMA21 AND Close < VWAP AND RSI < 40
        self.signals['short_entry'] = (
            (self.data['EMA9'] < self.data['EMA21']) &
            (self.data['close'] < self.data['VWAP']) &
            (self.data['RSI'] < 40)
        )

        return self.signals
