class MonitoringAgent:
    def __init__(self):
        self.active_positions = {}

    def track_position(self, symbol: str, entry_price: float, current_sl: float, target: float):
        self.active_positions[symbol] = {
            "entry": entry_price,
            "sl": current_sl,
            "target": target
        }

    def check_market_conditions(self, symbol: str, ltp: float):
        """
        Dynamically adjusts SL based on profit (Trailing SL logic)
        """
        if symbol not in self.active_positions:
            return None

        pos = self.active_positions[symbol]

        # Example: Move SL to breakeven if price moves 50% towards target
        distance_to_target = pos['target'] - pos['entry']
        if (ltp - pos['entry']) >= (distance_to_target * 0.5):
            if pos['sl'] < pos['entry']: # Only if SL is below entry (Long position)
                old_sl = pos['sl']
                pos['sl'] = pos['entry']
                return f"Adjusted SL from {old_sl} to Breakeven {pos['entry']}"

        return None
