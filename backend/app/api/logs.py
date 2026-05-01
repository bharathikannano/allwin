from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_trade_logs():
    return {
        "status": "success",
        "logs": [
            {
                "id": "1",
                "symbol": "BANKNIFTY",
                "entry_time": "2023-10-25T09:15:00Z",
                "exit_time": "2023-10-25T10:30:00Z",
                "entry_reason": "VWAP Crossover",
                "exit_reason": "Target Hit",
                "strategy": "Momentum",
                "gross_pnl": 1000,
                "net_pnl": 950,
                "charges": 50
            }
        ]
    }
