# Full-Stack Trading Dashboard

A high-performance full-stack trading dashboard for Indian markets with backtesting, paper trading, and live trading capabilities integrated with the Fyers API.

## Architecture

- **Backend**: Python, FastAPI, Pandas, TA-Lib, SQLAlchemy
- **Frontend**: React, Vite, TypeScript, Tailwind CSS

## Prerequisites

Before installing the Python dependencies, you must install the `ta-lib` C library system-wide.

### Installing TA-Lib C Library (Linux)

```bash
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar -xzf ta-lib-0.4.0-src.tar.gz
cd ta-lib
./configure --prefix=/usr
make
sudo make install
```

## Setup & Running

### Backend

1. Navigate to the `backend` directory.
2. Create and activate a virtual environment.
3. Install dependencies: `pip install -r requirements.txt`.
4. Run the server: `export PYTHONPATH=$(pwd) && uvicorn app.main:app` or `uvicorn app.main:app --reload`.

To run tests:
```bash
export PYTHONPATH=$(pwd)
pytest
```

### Frontend

1. Navigate to the `frontend` directory.
2. Install dependencies: `npm install`.
3. Run the development server: `npm run dev`.

## Philosophy
Strategies and algorithms avoid unrealistic 'guaranteed profits' and focus strictly on risk-adjusted net profitability, high-probability setups, and consistent performance after brokerage and taxes. The UI is designed to be a clean, minimal, 'fintech-grade' interface with smooth real-time updates.
