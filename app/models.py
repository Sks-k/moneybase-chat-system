import uuid
import time

class ChatSession:

    def __init__(self):
        self.session_id = str(uuid.uuid4())
        self.assigned_agent = None
        self.last_poll = time.time()
        self.active = True


class Agent:

    multipliers = {
        "junior": 0.4,
        "mid": 0.6,
        "senior": 0.8,
        "lead": 0.5
    }

    def __init__(self, name, level):

        self.name = name
        self.level = level
        self.capacity = int(10 * self.multipliers[level])
        self.active_chats = 0
