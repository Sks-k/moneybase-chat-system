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
