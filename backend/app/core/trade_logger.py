import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TradeLogger:
    def __init__(self):
        # In a real app, this would use a database
        self.logs = []

    def log_trade(self, symbol: str, strategy: str, entry_time: datetime, exit_time: datetime,
                  entry_reason: str, exit_reason: str, gross_pnl: float, net_pnl: float, charges: float):
        trade_record = {
            "id": str(len(self.logs) + 1),
            "symbol": symbol,
            "strategy": strategy,
            "entry_time": entry_time.isoformat(),
            "exit_time": exit_time.isoformat(),
            "entry_reason": entry_reason,
            "exit_reason": exit_reason,
            "gross_pnl": gross_pnl,
            "net_pnl": net_pnl,
            "charges": charges
        }
        self.logs.append(trade_record)
        logger.info(f"Trade Logged: {symbol} | Net PnL: {net_pnl} | Reason: {exit_reason}")
        return trade_record

    def get_logs(self):
        return self.logs
