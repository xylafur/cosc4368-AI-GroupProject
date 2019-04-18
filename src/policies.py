"""
    These modules should return the next action that should be taken given the
    current state of the agent and the positions around the agent in the world.
"""

import random

from manager import get_current_state
from qtable import get_max_neighbors

PRANDOM = "PRANDOM"
PEPLOIT = "PEPLOIT"
PGREEDY = "PGREEDY"

def p_random(agent, world, qtable, state_space='big'):
    neighbors = world.get_neighbors(*agent.get_position())
    #check all of the neighboring points to see if we can pick up or drop off
    for _dir, pos in neighbors.items():
        if world.is_pickup(*pos) and not agent.is_holding_block():
            return _dir
        elif world.is_dropoff(*pos) and agent.is_holding_block():
            return _dir

    return random.choice(list(neighbors.keys()))

def p_greedy(agent, world, qtable, state_space='big'):
    neighbors = world.get_neighbors(*agent.get_position())

    for _dir, pos in neighbors.items():
        if world.is_pickup(*pos) and not agent.is_holding_block():
            return _dir
        elif world.is_dropoff(*pos) and agent.is_holding_block():
            return _dir

    return random.choice(get_max_neighbors(
        neighbors, get_current_state(world, agent, state_space=state_space),
        qtable))

def p_exploit(agent, world, qtable, state_space='big'):
    neighbors = world.get_neighbors(*agent.get_position())

    for _dir, pos in neighbors.items():
        if world.is_pickup(*pos) and not agent.is_holding_block():
            return _dir
        elif world.is_dropoff(*pos) and agent.is_holding_block():
            return _dir

    r = random.randint(1, 10)
    if r <= 8:
        return random.choice(get_max_neighbors(
            neighbors, get_current_state(world, agent, state_space=state_space),
            qtable))
    else:
        #because I'm lazy
        return p_random(agent, world, qtable)
