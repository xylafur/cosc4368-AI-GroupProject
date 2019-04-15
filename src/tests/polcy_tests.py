
from test import test, TESTS
from world import World
from agent import Agent
from policies import p_random

@test
def p_random_test():
    agent = Agent(3, 3)
    world = World(5, 5, [(1, 1, 3)], [(1, 2, 3)], -1, 13, 13)


    assert(p_random(agent, world) in ["north", "south", "east", "west"])

    world = World(5, 5, [(4, 3, 3)], [(1, 1, 3)],-1, 13, 13)

    assert(p_random(agent, world) == "east")

    agent.pick_up()
    agent._set_position(1, 2)
    assert(p_random(agent, world) == "north")




