#!/bin/bash

# Exit on error
set -e

echo "Starting installation process..."

# Install backend dependencies
echo "Installing backend dependencies..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd ..

# Install frontend dependencies
echo "Installing frontend dependencies..."
cd frontend
npm install
cd ..

echo "Installation complete! You can now run the application using ./start.sh"
