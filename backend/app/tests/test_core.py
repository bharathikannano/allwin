import pandas as pd
import numpy as np
from app.core.strategy_engine import StrategyEngine
from app.core.risk_manager import RiskManager

def test_strategy_engine():
    # Create dummy data
    dates = pd.date_range("2023-01-01", periods=100)
    data = pd.DataFrame({
        'close': np.random.randn(100).cumsum() + 100,
        'high': np.random.randn(100).cumsum() + 105,
        'low': np.random.randn(100).cumsum() + 95,
        'volume': np.random.randint(1000, 10000, 100)
    }, index=dates)

    engine = StrategyEngine(data)
    signals = engine.apply_momentum_strategy()
    assert 'long_entry' in signals.columns
    assert 'short_entry' in signals.columns

def test_risk_manager():
    rm = RiskManager(account_balance=100000, risk_per_trade_pct=1.0)

    # 1% risk on 100k = 1000. Risk per share = 10 (100 - 90)
    size = rm.calculate_position_size(entry_price=100, stop_loss=90)
    assert size == 100

    # Check net pnl
    pnl = rm.calculate_net_pnl(gross_pnl=5000, turnover=500000, is_options=True)
    assert pnl['net_pnl'] < 5000
    assert pnl['charges'] > 0

if __name__ == '__main__':
    test_strategy_engine()
    test_risk_manager()
    print("Tests passed")
