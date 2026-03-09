import time
from app.queue_manager import dequeue_chat, SESSION_STORE
from app.assignment import find_available_agent

def assignment_worker():

    while True:

        session_id = dequeue_chat()

        if session_id:

            agent = find_available_agent()

            if agent:
                agent.active_chats += 1
                SESSION_STORE[session_id].assigned_agent = agent.name

        time.sleep(1)
