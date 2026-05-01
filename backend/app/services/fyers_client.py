import os
import json
from datetime import datetime
from fyers_apiv3 import fyersModel

# Mock/placeholder values for Fyers Integration.
# In a real environment, these would be loaded from a .env file or a secure vault.
FYERS_CLIENT_ID = os.getenv("FYERS_CLIENT_ID", "dummy_client_id")
FYERS_SECRET_KEY = os.getenv("FYERS_SECRET_KEY", "dummy_secret_key")
FYERS_REDIRECT_URI = os.getenv("FYERS_REDIRECT_URI", "http://localhost:8000/api/fyers/callback")

class FyersClientManager:
    def __init__(self):
        self.access_token = self._load_token()
        self.fyers = None
        if self.access_token:
            self.fyers = fyersModel.FyersModel(client_id=FYERS_CLIENT_ID, token=self.access_token, is_async=False, log_path="")

    def _load_token(self):
        """Loads token securely from storage."""
        try:
             with open("fyers_token.json", "r") as f:
                  data = json.load(f)
                  return data.get("access_token")
        except FileNotFoundError:
            return None

    def save_token(self, token: str):
        """Saves token securely."""
        self.access_token = token
        self.fyers = fyersModel.FyersModel(client_id=FYERS_CLIENT_ID, token=self.access_token, is_async=False, log_path="")
        with open("fyers_token.json", "w") as f:
             json.dump({"access_token": token, "updated_at": datetime.now().isoformat()}, f)

    def generate_auth_url(self) -> str:
        """Generate login URL for Fyers Auth."""
        session = fyersModel.SessionModel(
            client_id=FYERS_CLIENT_ID,
            secret_key=FYERS_SECRET_KEY,
            redirect_uri=FYERS_REDIRECT_URI,
            response_type="code",
            grant_type="authorization_code"
        )
        return session.generate_authcode()

    def generate_token_from_code(self, auth_code: str):
        """Generate Access Token from Auth Code."""
        session = fyersModel.SessionModel(
            client_id=FYERS_CLIENT_ID,
            secret_key=FYERS_SECRET_KEY,
            redirect_uri=FYERS_REDIRECT_URI,
            response_type="code",
            grant_type="authorization_code"
        )
        session.set_token(auth_code)
        response = session.generate_token()
        if response.get("s") == "ok":
            access_token = response["access_token"]
            self.save_token(access_token)
            return True, "Login successful"
        return False, response.get("message", "Login failed")

    def get_live_market_data(self, symbols: list):
        """Fetch real-time data."""
        if not self.fyers:
            return {"status": "error", "message": "Not authenticated"}

        data = {"symbols": ",".join(symbols)}
        response = self.fyers.quotes(data=data)
        return response

    def place_order(self, symbol: str, qty: int, side: int, order_type: int, product_type: str, price: float = 0):
        """Place an order through Fyers."""
        if not self.fyers:
            return {"status": "error", "message": "Not authenticated"}

        data = {
            "symbol": symbol,
            "qty": qty,
            "type": order_type,
            "side": side,
            "productType": product_type,
            "limitPrice": price,
            "stopPrice": 0,
            "validity": "DAY",
            "disclosedQty": 0,
            "offlineOrder": False,
        }

        response = self.fyers.place_order(data=data)
        return response

fyers_manager = FyersClientManager()
