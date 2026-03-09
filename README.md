# Chat Support Queue System

Backend implementation of the coding task.

## Features

- FIFO queue for chat sessions
- Redis based queue
- Agent assignment with round robin preference
- Capacity based on seniority
- Queue limit = team capacity × 1.5
- Poll monitoring
- Overflow team during office hours
- Dockerized deployment

## Architecture

Client → FastAPI → Redis Queue → Assignment Worker → Agents

## Run

docker-compose up --build

API Docs

http://localhost:8000/docs



---

### Option 2 — Run Locally (Without Docker)
# I used option 2
To simplify local testing without Redis, the queue can run using an in-memory implementation.

Install dependencies:
pip install -r requirements.txt
