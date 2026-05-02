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

Follow these steps to set up and run the application.

### 1. Backend Installation

Open a terminal, navigate to the `backend` folder, and run the following commands to create a virtual environment and install dependencies:

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Frontend Installation

Open a new terminal window, navigate to the `frontend` folder, and install the Node dependencies:

```bash
cd frontend
npm install
```

### 3. Starting the Application

You need to run both the backend and frontend servers simultaneously.

**Start the Backend:**
In your backend terminal (with the virtual environment activated):
```bash
cd backend
export PYTHONPATH=$(pwd)
uvicorn app.main:app
```

**Start the Frontend:**
In your frontend terminal:
```bash
cd frontend
npm run dev
```

*(Optional: If you are on a Mac/Linux machine with `bash` available, you can alternatively use `./install.sh` and `./start.sh` from the root directory to automate these steps).*

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
