#!/bin/bash

# Get absolute path to the project root
PROJECT_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Set up environment variables
export PATH="$PROJECT_ROOT/env/bin:$PATH"
export DATABASE_URL="sqlite:///$PROJECT_ROOT/cmis.db"
export PYTHONPATH="$PROJECT_ROOT/backend"

echo "Starting Backend..."
cd "$PROJECT_ROOT/backend"
# Start uvicorn in the background
uvicorn main:app --host 0.0.0.0 --port 8000 --reload &
BACKEND_PID=$!
echo "Backend started with PID $BACKEND_PID"

echo "Starting Frontend..."
cd "$PROJECT_ROOT/frontend"
npm run dev &
FRONTEND_PID=$!
echo "Frontend started with PID $FRONTEND_PID"

echo "Application running!"
echo "Backend: http://localhost:8000"
echo "Frontend: http://localhost:3000"
echo "Press CTRL+C to stop both."

# Trap SIGINT to kill both processes
trap "kill $BACKEND_PID $FRONTEND_PID; exit" SIGINT

wait
