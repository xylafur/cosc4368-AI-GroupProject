"""
    There is still alot that needs to be done for this module!
"""

import itertools

class QTable:
    def __init__(self, world):
        self._w = world.get_width()
        self._h = world.get_height()

        self._table = {}

        self.state_space = [
            [w for w in range(self._w)],
            [h for h in range(self._h)],
            [True, False],
        ]
        #idk how to do this with list comprehension
        for ii in range(world.num_pickup_locations() + world.num_dropoff_locations()):
            self.state_space.append([True, False])

        #initialize all values in the table to 0
        for state in itertools.product(*self.state_space):
            if world.is_pickup(state[0], state[1]):
                self._table[state] = 'pickup'
            elif world.is_dropoff(state[0], state[1]):
                self._table[state] = 'dropoff'
            else:
                self._table[state] = {
                    'north': 0,
                    'south': 0,
                    'east': 0,
                    'west': 0
                }

    def __repr__(self):
        s = 'x  y  holding block'
        for state in itertools.product(*self.state_space):
            s += "{} = {}\n".format(state, self._table[state])
        return s

    def __getitem__(self, state):
        return self._table[state]


    def update_table(self, state, vals):
        """
            Vals is expected to be a dict with keys north, south east and west,
            up to two of these can be missing at a time (corner blocks)
        """
        self._table[state] = vals.copy()




