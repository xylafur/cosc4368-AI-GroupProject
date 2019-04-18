"""
    There is still alot that needs to be done for this module!
"""

import itertools
import random

adjacent_state = lambda x, y, current_state: (x, y) + current_state[2:]

def get_adjacent_states(neighbors, current_state):
    """
        Takes in a dict of neighbors
            {'north': (3, 2), 'south': (3, 4) ....}
        and the current state
            (3, 3, False, True, ..... )

        Returns a list of the neighbors in state form
            [ (3, 2, False, True, .....), (3, 4, False, True, ....) ]
    """
    adj = []
    for v in neighbors.values():
        adj.append(adjacent_state(*v, current_state))
    return adj

def get_max_neighbors(neighbors, current_state, qtable):
    """
        Returns a list of (x, y) points representing the neighbors that have
        the highest q value

        Examples of return:
            [(2, 2), (2, 3)]    #tied for max
            [(5, 5)]            #only one max
    """
    r = random.choice(list(neighbors.keys()))
    max_val = qtable[current_state][r]
    max_neighbors = [r]

    for direction in neighbors.keys():
        if direction in max_neighbors:
            continue

        if qtable[current_state][direction] > max_val:
            max_val = qtable[current_state][direction]
            max_neighbors = [direction]

        elif qtable[current_state][direction] == max_val:
            max_neighbors.append(direction)

    return max_neighbors

class QTable:
    def __init__(self, world, state_space='big'):
        self._w = world.get_width()
        self._h = world.get_height()

        self._table = {}

        self._state_space = state_space

        self.state_space = [
            [w for w in range(self._w)],
            [h for h in range(self._h)],
            [True, False],
        ]

        if state_space == 'big':
            #idk how to do this with list comprehension
            for ii in range(world.num_pickup_locations() + world.num_dropoff_locations()):
                self.state_space.append([True, False])

        self._num_pickup = world.num_pickup_locations()

        self._num_dropoff = world.num_dropoff_locations()



       #initialize all values in the table to 0
        for state in itertools.product(*self.state_space):
            self._table[state] = {
                'north': 0,
                'south': 0,
                'east': 0,
                'west': 0
            }

            if world.is_pickup(state[0], state[1]):
                self._table[state]['type'] = 'pickup'
            elif world.is_dropoff(state[0], state[1]):
                self._table[state]['type'] = 'dropoff'
            else:
                self._table[state]['type'] = 'normal'

            self._table[state]['touched'] = False


    def __repr__(self):
        s = ''

        #print it out in a better order
        if self._state_space == 'big':
            pickup_dropoff = [[True, False] for _ in range(self._num_pickup +
                                                           self._num_dropoff)]

            for pd_s in itertools.product(*pickup_dropoff):
                for holding_block in [True, False]:
                    for x in range(self._w):
                        for y in range(self._h):
                            state = (x, y, holding_block) + tuple(pd_s)

                            if any([v != 0 for k, v in self._table[state].items()
                                    if k in ['north', 'south', 'east', 'west']]):
                                self._table[state]['touched'] = True

                            s += "{} = {}\r\n".format(state, self[state])

                s += "\r\n"
        else:
            for holding_block in [True, False]:
                for x in range(self._w):
                    for y in range(self._h):
                        state = (x, y, holding_block)
                        if any([v != 0 for k, v in self._table[state].items()
                                if k in ['north', 'south', 'east', 'west']]):
                            self._table[state]['touched'] = True

                        s += "{} = {}\r\n".format(state, self[state])

        return s

    def __getitem__(self, state):
        return self._table[state]

    def __setitem__(self, state, val):
        self._table[state] = val


    def update_table(self, state, vals):
        """
            Vals is expected to be a dict with keys north, south east and west,
            up to two of these can be missing at a time (corner blocks)
        """
        self._table[state] = vals.copy()




