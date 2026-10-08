# -*- coding: utf-8 -*-
"""
Project: Crypto 5-Min Short-Term Quant & Event Bot
Target Symbols: BTC-USDT, ETH-USDT (5m Timeframe)
Description: Main execution loop for short-term momentum and breakout strategy.
"""

import time
import sys
import os
from src.logger import logger
from src.api_client import HibtApiClient
from src.strategy import ShortTermMomentumStrategy

def run_trading_bot():
    logger.info("==================================================")
    logger.info("Initializing 5-Min Strategy Bot for BTC & ETH...")
    logger.info("==================================================")
    
    api_key = os.getenv("HIBT_API_KEY", "demo_key_btc_eth")
    secret_key = os.getenv("HIBT_SECRET_KEY", "demo_secret_5m")
    
    client = HibtApiClient(api_key=api_key, secret_key=secret_key)
    
    symbols = ["BTC-USDT", "ETH-USDT"]
    strategies = {sym: ShortTermMomentumStrategy(symbol=sym, timeframe="5m") for sym in symbols}
    
    try:
        server_status = client.get_server_time()
        logger.info(f"API Connection verified. Exchange Time Sync: {server_status}")
        
        logger.info("Starting 5-minute candle evaluation loop...")
        for step in range(1, 4):
            logger.info(f"=== Market Polling Cycle #{step} ===")
            
            market_data = {
                "BTC-USDT": {"close": 65200.0 + (step * 80), "high": 65350.0, "low": 65100.0, "volume": 124.5},
                "ETH-USDT": {"close": 3450.0 + (step * 15), "high": 3475.0, "low": 3440.0, "volume": 850.2}
            }
            
            for sym in symbols:
                current_candle = market_data[sym]
                logger.info(f"Analyzing {sym} [5m] -> Close: {current_candle['close']}, Vol: {current_candle['volume']}")
                strategies[sym].on_bar_close(current_candle)
            
            if step < 3:
                logger.info("Waiting for next 5-minute interval simulation...\n")
                time.sleep(2)
                
        logger.info("5-min strategy background test completed successfully.")
        
    except Exception as e:
        logger.error(f"Critical error in execution loop: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    run_trading_bot()
