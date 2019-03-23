#!/usr/bin/env python3

"""
    This module has the implementation for everything related to the world
    itself.

                    North
                 0  1  2  3  4
            0   [X, X, X, X, X]
            1   [X, X, X, X, X]
    West    2   [X, X, X, X, X]     east
            3   [X, X, X, X, X]
            4   [X, X, X, X, X]
                    South
"""


from location import PickUpLocation, DropOffLocation, NormalLocation

class World:
    def __init__(self, width, height, pick_up_locations, drop_off_locations,
                 reward, pick_up_reward, drop_off_reward):
        """
            Parameters:
                width (int)
                    the width of the world

                height (int)
                    the height of the world

                pick_up_locations (list of tuples)
                    a list of the (x, y, n) positions of all of the drop off
                    locations and the number of blocks they contain

                drop_off_locations (list of tuples)
                    a list of the (x, y, c) positiohns of all pick up locations
                    and the maximum number of blocks each of them can hold

                reward (int)
                    the reward to the agent for normal blocks, or when the
                    agent lands on a pick up / drop off but cant pick up / drop
                    off

                pick_up_reward (int)
                    the reward to the agent when it picks up a block

                drop_off_reward (int)
                    the reward to the agent when it drops off a block
        """
        #initially populate the grid just with normal locations
        self._grid = [[NormalLocation(reward) for _ in range(width)] for _ in range(height)]

        for (x, y, n) in pick_up_locations:
            self._grid[y][x] = PickUpLocation(pick_up_reward, reward, n)

        for (x, y, c) in drop_off_locations:
            self._grid[y][x] = DropOffLocation(drop_off_reward, reward, c)

        self._w = width
        self._h = height

    def __repr__(self):
        s = ''
        for l in self._grid:
            s += str(l) + '\n'
        return s

    def get_square(self, x, y):
        assert(x < self._w)
        assert(y < self._h)
        return self._grid[y][x]

    def get_neighbors(self, x, y):
        """
            Returns:
                A dict containing all of the valid neighbors of a particular
                square.  If that square is somewhere in the center then the
                return dict will contain 'north', 'south', 'east' and 'west'

                The values in the dict is the (x, y) position of each of the
                neighbors
        """
        D = {}
        if x > 0:
            D['west'] = (x-1, y)
        if x < (self._w - 1):
            D['east'] = (x+1, y)
        if y > 0:
            D['south'] = (x, y+1)
        if y < (self._h - 1):
            D['north'] = (x, y-1)
        return D

    def is_pickup(self, x, y):
        return self.get_square(x, y).is_pickup()

    def is_dropoff(self, x, y):
        return self.get_square(x, y).is_dropoff()

    def get_reward(self, x, y, has_block):
        return self.get_square(x, y).get_reward(has_block)

    # The below functions assume that the user knows that this particular
    # square is of the correct type
    def check_pick_up(self, x, y):
        return self.get_square(x, y).check_pick_up()

    def check_drop_off(self, x, y):
        return self.get_square(x, y).check_drop_off()

    def pick_up(self, x, y):
        self.get_square(x, y).pick_up()

    def drop_off(self, x, y):
        self.get_square(x, y).drop_off()

