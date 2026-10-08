# -*- coding: utf-8 -*-
from src.logger import logger

class ShortTermMomentumStrategy:
    def __init__(self, symbol: str, timeframe: str = "5m"):
        self.symbol = symbol
        self.timeframe = timeframe
        self.price_history = []
        logger.info(f"Initialized Short-Term Momentum Strategy for {symbol} on {timeframe} chart.")

    def calculate_ema(self, prices, period=9):
        if len(prices) < period:
            return prices[-1] if prices else 0
        multiplier = 2 / (period + 1)
        ema = prices[0]
        for price in prices[1:]:
            ema = (price - ema) * multiplier + ema
        return ema

    def on_bar_close(self, candle_data: dict):
        close_price = candle_data["close"]
        self.price_history.append(close_price)
        
        if len(self.price_history) > 20:
            self.price_history.pop(0)

        logger.info(f"[{self.symbol}] 5m Bar Closed. Price: {close_price}")

        if len(self.price_history) >= 5:
            short_ema = self.calculate_ema(self.price_history, period=5)
            logger.info(f"[{self.symbol}] Calculated 5m EMA(5): {short_ema:.2f}")

            if close_price > short_ema * 1.002:
                logger.warning(f"[SIGNAL - BUY] {self.symbol} broke above 5m EMA! Potential upward momentum.")
            elif close_price < short_ema * 0.998:
                logger.warning(f"[SIGNAL - SELL] {self.symbol} fell below 5m EMA! Potential downward pressure.")
            else:
                logger.info(f"[{self.symbol}] Market consolidating. Waiting for clear 5m breakout.")
