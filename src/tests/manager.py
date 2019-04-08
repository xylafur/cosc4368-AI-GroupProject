from test import test, TESTS
from world import World
from agent import Agent

from manager import manager, get_current_state

@test
def get_current_state_test():
    w = World(5, 5, [(1, 1, 3), (2, 2, 4)], [(3, 3, 3), (4, 4, 4)], -1, 13, 13)
    a = Agent(0, 0)

    assert(get_current_state(w, a) == (0, 0, False, True, True, True, True))

    a._set_position(3, 3)
    w.pick_up(1, 1)
    w.pick_up(1, 1)
    w.pick_up(1, 1)

    assert(get_current_state(w, a) == (3, 3, False, False, True, True, True))

