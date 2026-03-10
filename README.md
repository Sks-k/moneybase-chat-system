# Chat Support Queue System

Backend implementation of the chat support system coding task.

This service simulates a customer support backend where users initiate chat sessions and the system assigns them to available agents based on their capacity and seniority.

---

## Features

- FIFO queue for chat sessions
- Redis-based queue for distributed processing
- Agent assignment with round-robin preference
- Capacity calculation based on seniority multipliers
- Queue limit = team capacity × 1.5
- Session polling monitoring
- Overflow team support during office hours
- Dockerized deployment support
- Local testing support without Redis

---

## Architecture

Client → FastAPI → Redis Queue → Assignment Worker → Agents

The system processes chat requests through a queue and assigns them to agents depending on their availability and efficiency.

---

## Queue Implementation

The system is designed to use Redis for distributed queue processing.

For easier local testing without Docker, an in-memory queue implementation is used as a fallback.

In production environments, Redis should be used to support distributed workers and horizontal scaling.

## Agent Capacity

Each agent can handle up to **10 concurrent chats**, multiplied by their efficiency level.


Queue limit:

```
queue_size = team_capacity × 1.5
```

---

## API Endpoints

### Create Chat Session

```
POST /chat/start
```

Creates a new chat session and places it in the queue.

---

### Poll Session

```
GET /chat/{session_id}/poll
```

Client polling endpoint used to keep the session active.

---

### Health Check

```
GET /health
```

Returns service health status.

---

### Metrics

```
GET /metrics
```

Returns system metrics such as queue length and active sessions.

---

## Run the Project

### Option 1 — Using Docker (Recommended)

Run the application using Docker:

```
docker-compose up --build
```

Open API documentation:

```
http://localhost:8000/docs
```

---

### Option 2 — Run Locally (Without Docker)

For easier local testing, the system can run without Redis by using an **in-memory queue implementation**.

Install dependencies:

```
pip install -r requirements.txt
```

Start the API server:

```
uvicorn app.main:app --reload
```

Open API documentation:

```
http://127.0.0.1:8000/docs
```

---

## Design Considerations

- FIFO queue ensures fair ordering of chat requests.
- Junior agents are prioritized so senior agents remain available to assist when needed.
- Agent capacity is calculated dynamically based on efficiency multipliers.
- Session monitoring detects inactive sessions when polling stops.
- Overflow team helps handle spikes in demand during office hours.

---

## Possible Improvements

- WebSocket based real-time chat instead of polling
- Redis Streams or Kafka for large-scale message processing
- Kubernetes deployment
- Prometheus and Grafana monitoring
