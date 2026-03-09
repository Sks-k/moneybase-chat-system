import redis

r = redis.Redis(host="redis", port=6379, decode_responses=True)

SESSION_STORE = {}

QUEUE_NAME = "chat_queue"

def enqueue_chat(session_id):
    r.rpush(QUEUE_NAME, session_id)

def dequeue_chat():
    return r.lpop(QUEUE_NAME)

def queue_length():
    return r.llen(QUEUE_NAME)
