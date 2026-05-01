from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel
from app.services.fyers_client import fyers_manager

router = APIRouter()

class OrderRequest(BaseModel):
    symbol: str
    qty: int
    side: int # 1 for Buy, -1 for Sell
    order_type: int # 1 for Limit, 2 for Market, etc.
    product_type: str # INTRADAY, CNC, MARGIN
    price: float = 0

@router.get("/login")
def get_login_url():
    """Returns the Fyers Auth URL."""
    auth_url = fyers_manager.generate_auth_url()
    return {"status": "success", "auth_url": auth_url}

@router.get("/callback")
def handle_callback(auth_code: str = None, s: str = None, code: str = None):
    """Callback URL for Fyers Auth."""
    # Fyers API passes auth_code in the query parameters
    code_to_use = auth_code or code
    if not code_to_use:
         raise HTTPException(status_code=400, detail="Missing auth_code")

    success, msg = fyers_manager.generate_token_from_code(code_to_use)
    if success:
        return {"status": "success", "message": "Successfully authenticated with Fyers"}
    else:
        raise HTTPException(status_code=400, detail=msg)

@router.get("/market-data")
def get_market_data(symbols: str):
    """Fetch live market data. symbols should be comma-separated."""
    symbol_list = symbols.split(",")
    data = fyers_manager.get_live_market_data(symbol_list)
    return data

@router.post("/execute")
def execute_trade(req: OrderRequest):
    """Execute a live trade."""
    response = fyers_manager.place_order(
        symbol=req.symbol,
        qty=req.qty,
        side=req.side,
        order_type=req.order_type,
        product_type=req.product_type,
        price=req.price
    )
    return {"status": "success", "fyers_response": response}

@router.get("/positions")
def get_live_positions():
    """Get active live positions (Mocked for now)."""
    return {
        "status": "success",
        "positions": []
    }
