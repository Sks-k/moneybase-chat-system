from collections import deque

chat_queue = deque()

SESSION_STORE = {}

def enqueue_chat(session_id):
    chat_queue.append(session_id)

def dequeue_chat():

    if chat_queue:
        return chat_queue.popleft()

    return None


def queue_length():
    return len(chat_queue)
