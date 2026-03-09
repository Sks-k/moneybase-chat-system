import time
from app.queue_manager import SESSION_STORE

def monitor_sessions():

    while True:

        now = time.time()

        for s in list(SESSION_STORE.values()):

            if now - s.last_poll > 3:
                s.active = False

        time.sleep(1)
