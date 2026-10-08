import hmac
import hashlib
import time
import requests

class HibtApiClient:
    def __init__(self, api_key, secret_key, base_url="https://api.hibt.com"):
        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = base_url

    def _generate_signature(self, params_str):
        return hmac.new(
            self.secret_key.encode('utf-8'),
            params_str.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

    def get_server_time(self):
        url = f"{self.base_url}/api/v1/time"
        response = requests.get(url, timeout=5)
        return response.json()
