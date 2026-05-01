from fastapi import APIRouter

router = APIRouter()

@router.get("/positions")
def get_paper_positions():
    return {
        "status": "success",
        "positions": [
            {"symbol": "NIFTY", "qty": 50, "entry_price": 21000, "ltp": 21050, "pnl": 2500}
        ]
    }
