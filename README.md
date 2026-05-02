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

We have provided convenient scripts to install and run both the frontend and backend simultaneously.

### One-Command Installation

To install all dependencies for both the backend and frontend at once, run:

```bash
./install.sh
```

### One-Command Start

To start both the backend API server and the frontend development server concurrently, run:

```bash
./start.sh
```

The frontend will be available at `http://localhost:5173` and the backend API at `http://localhost:8000`.

### Running Tests

To run the backend test suite:
```bash
cd backend
source venv/bin/activate
export PYTHONPATH=$(pwd)
pytest
```

## Philosophy
Strategies and algorithms avoid unrealistic 'guaranteed profits' and focus strictly on risk-adjusted net profitability, high-probability setups, and consistent performance after brokerage and taxes. The UI is designed to be a clean, minimal, 'fintech-grade' interface with smooth real-time updates.
