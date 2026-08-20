#!/bin/bash

echo "=== DevOps Task Manager - Startup Script ==="

APP_FILE="app.py"
PORT=5001

# Check if app.py exists
if [ ! -f "$APP_FILE" ]; then
    echo "Error: $APP_FILE not found!"
    exit 1
fi

# Check if port is already in use
if lsof -i :$PORT >/dev/null 2>&1; then
    echo "Port $PORT is already in use. Stopping existing process..."
    kill $(lsof -t -i :$PORT)
    sleep 1
fi

echo "Starting Flask application on port $PORT..."
python3 "$APP_FILE" &
APP_PID=$!

sleep 2

echo "Checking if app is running (PID: $APP_PID)..."
if ps -p $APP_PID > /dev/null; then
    echo "✅ App started successfully."
    curl -s http://localhost:$PORT/ 
    echo ""
    echo "System info:"
    echo "Date: $(date)"
    echo "User: $(whoami)"
    echo "Host: $(hostname)"
else
    echo "❌ App failed to start."
    exit 1
fi