from world import World
from agent import Agent
from qtable import QTable, get_adjacent_states, get_max_neighbors, adjacent_state
from manager import get_current_state

from test import test, TESTS

@test
def state_space_present_test():
    w = World(5, 5, [(1, 1, 3), (2, 2, 4)], [(3, 3, 3), (4, 4, 4)], -1, 13, 13)
    q = QTable(w)

    assert(len(q._table) == 5 * 5 * 2 * 2 * 2 * 2 * 2)

@test
def state_lookup():
    w = World(5, 5, [(1, 1, 3), (2, 2, 4)], [(3, 3, 3), (4, 4, 4)], -1, 13, 13)
    q = QTable(w)
    a = Agent(0, 0)

    state = get_current_state(w, a)

    assert(q[state] == {'north': 0, 'south': 0, 'east': 0, 'west': 0})

@test
def get_adjacent_states_test():
    a = Agent(3, 3)
    w = World(5, 5, [(1, 1, 3), (2, 2, 4)], [(3, 3, 3), (4, 4, 4)], -1, 13, 13)
    adj = get_adjacent_states(w.get_neighbors(3, 3), get_current_state(w, a))


    assert((3, 4, False, True, True, True, True) in adj)
    assert((3, 4, False, True, True, True, True) in adj)
    assert((3, 4, False, True, True, True, True) in adj)
    assert((3, 4, False, True, True, True, True) in adj)

@test
def get_max_neighbors_test():
    a = Agent(3, 2)
    w = World(5, 5, [(1, 1, 3), (2, 2, 4)], [(3, 3, 3), (4, 4, 4)], -1, 13, 13)
    q = QTable(w)

    q[get_current_state(w, a)]['south'] = 13

    assert(get_max_neighbors(w.get_neighbors(*a.get_position()),
                             get_current_state(w, a), q) == ['south'])

