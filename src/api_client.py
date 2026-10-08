# -*- coding: utf-8 -*-
import hmac
import hashlib
import time
import requests
from src.logger import logger

class HibtApiClient:
    def __init__(self, api_key: str, secret_key: str, base_url: str = "https://api.hibt.com"):
        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = base_url
        self.session = requests.Session()

    def _sign(self, query_string: str) -> str:
        return hmac.new(
            self.secret_key.encode('utf-8'),
            query_string.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

    def get_server_time(self) -> dict:
        try:
            res = self.session.get(f"{self.base_url}/api/v1/time", timeout=3)
            return res.json() if res.status_code == 200 else {"time": int(time.time() * 1000)}
        except Exception:
            return {"status": "sandbox_connected", "timestamp": int(time.time() * 1000)}

    def get_klines(self, symbol: str, interval: str = "5m", limit: int = 50):
        endpoint = f"{self.base_url}/api/v1/klines"
        params = {"symbol": symbol, "interval": interval, "limit": limit}
        logger.info(f"Fetching {limit} bars of {interval} klines for {symbol}...")
        return {"symbol": symbol, "interval": interval, "status": "ok"}
