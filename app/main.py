from fastapi import FastAPI
import time
import threading

from app.models import ChatSession
from app.queue_manager import enqueue_chat, queue_length, SESSION_STORE
from app.agents import agents
from app.worker import assignment_worker
from app.monitor import monitor_sessions

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Moneybase Chat System Running"}

TEAM_CAPACITY = sum(a.capacity for a in agents)

MAX_QUEUE = int(TEAM_CAPACITY * 1.5)


@app.on_event("startup")
def startup():

    threading.Thread(target=assignment_worker, daemon=True).start()

    threading.Thread(target=monitor_sessions, daemon=True).start()


@app.post("/chat/start")
def start_chat():

    if queue_length() >= MAX_QUEUE:

        return {"status": "refused"}

    session = ChatSession()

    SESSION_STORE[session.session_id] = session

    enqueue_chat(session.session_id)

    return {

        "status": "ok",

        "session_id": session.session_id
    }


@app.get("/chat/{session_id}/poll")
def poll(session_id):

    if session_id not in SESSION_STORE:

        return {"status": "invalid"}

    SESSION_STORE[session_id].last_poll = time.time()

    return {"status": "active"}


@app.get("/health")
def health():

    return {"status": "healthy"}


@app.get("/metrics")
def metrics():

    return {

        "queue_length": queue_length(),

        "active_sessions": len(SESSION_STORE)
    }
