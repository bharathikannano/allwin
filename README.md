# Full-Stack Trading Dashboard

A high-performance full-stack trading dashboard for Indian markets with backtesting, paper trading, and live trading capabilities integrated with the Fyers API.

## Architecture

- **Backend**: Python, FastAPI, Pandas, TA-Lib, SQLAlchemy
- **Frontend**: React, Vite, TypeScript, Tailwind CSS

## Prerequisites

Before running the project, you must have the following installed on your machine:

1. **Python 3.8+**
2. **Node.js (18+) and npm**
3. **TA-Lib C Library** (Required for technical analysis calculations in the backend).

### Installing TA-Lib C Library (Linux)

To install the TA-Lib C library natively on Linux, run the following commands:

```bash
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar -xzf ta-lib-0.4.0-src.tar.gz
cd ta-lib
./configure --prefix=/usr
make
sudo make install
```

*(Note: MacOS users can typically install this via `brew install ta-lib`)*

## Installation & Setup

We have provided convenient scripts to install and run both the frontend and backend simultaneously in one command.

### 1. Installation

To install all dependencies for both the backend (Python virtual environment and packages) and frontend (Node modules), run the provided installation script:

```bash
# Make the script executable if it isn't already
chmod +x install.sh

# Run the install script
./install.sh
```

### 2. Starting the Application

To start both the backend API server (FastAPI on Uvicorn) and the frontend development server (Vite) concurrently, run:

```bash
# Make the script executable if it isn't already
chmod +x start.sh

# Run the start script
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
