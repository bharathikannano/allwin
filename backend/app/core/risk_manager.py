class RiskManager:
    def __init__(self, account_balance: float, risk_per_trade_pct: float = 1.0):
        self.account_balance = account_balance
        self.risk_per_trade_pct = risk_per_trade_pct
        self.max_drawdown_limit = 0.10 # 10%
        self.peak_balance = account_balance

    def calculate_position_size(self, entry_price: float, stop_loss: float) -> int:
        """
        Calculates position size based on account risk and trade risk.
        """
        risk_amount = self.account_balance * (self.risk_per_trade_pct / 100)
        risk_per_share = abs(entry_price - stop_loss)

        if risk_per_share == 0:
            return 0

        position_size = int(risk_amount / risk_per_share)
        return position_size

    def check_drawdown(self, current_balance: float) -> bool:
        """
        Returns True if trading should be halted due to max drawdown.
        """
        if current_balance > self.peak_balance:
            self.peak_balance = current_balance

        drawdown = (self.peak_balance - current_balance) / self.peak_balance
        return drawdown >= self.max_drawdown_limit

    def calculate_net_pnl(self, gross_pnl: float, turnover: float, is_options: bool = True) -> dict:
        """
        Estimates net PnL after typical Indian brokerage charges (Fyers/Zerodha style)
        """
        brokerage = min(20.0, turnover * 0.0003) * 2 # Entry + Exit
        stt = turnover * 0.000125 if is_options else turnover * 0.001
        exchange_txn_charge = turnover * 0.0005
        gst = (brokerage + exchange_txn_charge) * 0.18
        sebi_charges = turnover * 0.000001
        stamp_duty = turnover * 0.00003

        total_charges = brokerage + stt + exchange_txn_charge + gst + sebi_charges + stamp_duty
        net_pnl = gross_pnl - total_charges

        return {
            "gross_pnl": gross_pnl,
            "charges": total_charges,
            "net_pnl": net_pnl
        }
