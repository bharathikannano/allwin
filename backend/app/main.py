from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import dashboard, backtest, paper_trade, live_trade, logs

app = FastAPI(
    title="Trading Dashboard API",
    description="High-performance trading dashboard API",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(dashboard.router, prefix="/api/dashboard", tags=["Dashboard"])
app.include_router(backtest.router, prefix="/api/backtest", tags=["Backtest"])
app.include_router(paper_trade.router, prefix="/api/paper-trade", tags=["Paper Trade"])
app.include_router(live_trade.router, prefix="/api/live-trade", tags=["Live Trade"])
app.include_router(logs.router, prefix="/api/logs", tags=["Logs"])

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Trading Dashboard API is running."}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
