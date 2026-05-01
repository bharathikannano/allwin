from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_dashboard_summary():
    return {
        "status": "success",
        "data": {
            "total_pnl": 15000.50,
            "win_rate": 65.5,
            "active_positions": 2,
            "daily_drawdown": 1.2
        }
    }
