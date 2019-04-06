from agent import Agent
from world import World

from test import test, TESTS

@test
def agent_movement_test():
    a = Agent(0, 0)

    a.move("east")
    assert(a.get_position() == (1, 0))
    a.move("south")
    assert(a.get_position() == (1, 1))
    a.move("south")
    a.move("south")
    a.move("south")
    assert(a.get_position() == (1, 4))

@test
def pick_up_drop_off():
    a = Agent(0, 0)

    assert(not a.is_holding_block())

    a.pick_up()

    assert(a.is_holding_block())

    a.drop_off()

    assert(not a.is_holding_block())

@test
def agent_reset_test():
    a = Agent(0, 0)

    a.move("east")
    a.move("east")
    a.move("east")
    a.move("east")
    a.move("west")
    a.move("south")
    a.move("south")
    a.move("south")
    a.move("south")
    assert(a.get_position() != (0, 0))

    a.reset_to_start()

    assert(a.get_position() == (0, 0))
    assert(not a.is_holding_block())
