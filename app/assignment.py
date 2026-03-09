from datetime import datetime
from app.agents import agents, overflow_agents
from app.config import OFFICE_START, OFFICE_END

def office_hours():
    now = datetime.now().hour
    return OFFICE_START <= now <= OFFICE_END

def find_available_agent():

    priority = ["junior","mid","senior","lead"]

    for level in priority:

        for agent in agents:

            if agent.level == level and agent.active_chats < agent.capacity:
                return agent

    if office_hours():

        for agent in overflow_agents:

            if agent.active_chats < agent.capacity:
                return agent

    return None
