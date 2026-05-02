#!/bin/bash

# Ensure backend and frontend run and close together
trap "kill 0" SIGINT SIGTERM EXIT

echo "Starting the trading dashboard..."

# Start backend
echo "Starting backend server..."
cd backend
source venv/bin/activate
export PYTHONPATH=$(pwd)
uvicorn app.main:app --port 8000 &
cd ..

# Start frontend
echo "Starting frontend server..."
cd frontend
npm run dev &
cd ..

# Wait for background processes
wait
