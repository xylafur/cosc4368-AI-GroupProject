"""
    These modules should return the next action that should be taken given the
    current state of the agent and the positions around the agent in the world.
"""

import random

PRANDOM = "PRANDOM"
PEPLOIT = "PEPLOIT"
PGREEDY = "PGREEDY"

##################
#   I have no idea what these functions will actually need, this is up to the
#   implementer.  They can be changed based on what the designer requires
##################
def p_random(agent, world):
    neighbors = world.get_neighbors(*agent.get_position())
    #check all of the neighboring points to see if we can pick up or drop off
    for _dir, pos in neighbors.items():
        if world.is_pickup(*pos) and not agent.is_holding_block():
            return _dir
        elif world.is_dropoff(*pos) and agent.is_holding_block():
            return _dir

    return random.choice(list(neighbors.keys()))


def p_greedy(agent, world):
    raise NotImplementedError()

def p_exploit(agent, world):
    raise NotImplementedError()
