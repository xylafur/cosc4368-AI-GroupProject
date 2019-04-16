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
import copy

from location import PickUpLocation, DropOffLocation, NormalLocation, PICKUP, DROPOFF

class World:

###############################################################################
#   Special Functions
###############################################################################
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
        #######################################################################
        #   Save all of the initial variables
        #######################################################################
        self._reward = reward

        self._pick_up_locations = pick_up_locations
        self._org_pick_up_locations = copy.deepcopy(pick_up_locations)
        self._pick_up_reward = pick_up_reward

        self._drop_off_locations = drop_off_locations
        self._drop_off_reward = drop_off_reward
        self._org_drop_off_locations = copy.deepcopy(drop_off_locations)

        self._w = width
        self._h = height

        #######################################################################
        #   Create the Grid for the world.  Initially full of normal locations
        #   but then add in the pick up and drop off locations
        #######################################################################

        self._grid = [[NormalLocation(reward) for _ in range(width)]
                      for _ in range(height)]

        #TODO: add sanity check to make sure none of the pick up and drop off
        #      locations are the same
        self._set_locations(pick_up_locations, PICKUP)
        self._set_locations(drop_off_locations, DROPOFF)

        self._original_grid = copy.deepcopy(self._grid)

    def __repr__(self):
        s = ''
        for l in self._grid:
            s += str(l) + '\n'
        return s

###############################################################################
#   Public Functions
###############################################################################

    num_pickup_locations = lambda self: len(self._pick_up_locations)
    num_dropoff_locations = lambda self: len(self._drop_off_locations)

    is_pickup_type = lambda self, x, y: self.get_square(x, y).is_pickup()
    is_dropoff_type = lambda self, x, y: self.get_square(x, y).is_dropoff()

    is_pickup = lambda self, x, y:                                      \
        self.is_pickup_type(x, y) and self._check_pick_up(x, y)

    is_dropoff = lambda self, x, y:                                     \
        self.is_dropoff_type(x, y) and self._check_drop_off(x, y)


    # The below functions assume that the user knows that this particular
    # square is of the correct type
    _check_pick_up = lambda self, x, y: self.get_square(x, y).check_pick_up()
    _check_drop_off = lambda self, x, y: self.get_square(x, y).check_drop_off()


    get_reward = lambda self, x, y, has_block:                          \
        self.get_square(x, y).get_reward(has_block)

    get_block_count = lambda self, x, y, grid=None:                     \
        self.get_square(x, y, grid=grid).get_block_count()

    def locations_status(self, location_type):
        """
            Iterates through the world from left to right, top to bottom.

            Returns a list for each of the pick up locations where True
            represents the location still having blocks to be picked up and
            False means that the space is empty
        """
        assert(location_type in [PICKUP, DROPOFF])

        locs = []
        for x in range(self._w):
            for y in range(self._h):
                if location_type == PICKUP and self.is_pickup_type(x, y):
                    locs.append(self.is_pickup(x, y))
                elif location_type == DROPOFF and self.is_dropoff_type(x, y):
                    locs.append(self.is_dropoff(x, y))
        return locs

    _swapped = False
    def swap_pickup_dropoff(self, reset=True):
        """
            This function will make all old pick up locations drop off
            locations and vice versa

            It resets the world before doing the swap!

            Also it is intelligent (ooooh scary smary machine!).  If it has
            swaped the locations before, it will just reset the world (beause
            that makes it how it was in the beginning)
        """
        self.reset_world()

        if self._swapped:
            self._swapped = False
            return
        else:
            self._swapped = True

        self._pick_up_locations, self._drop_off_locations = \
                self._drop_off_locations, self._pick_up_locations

        self._set_locations(self._pick_up_locations, PICKUP)
        self._set_locations(self._drop_off_locations, DROPOFF)

    def get_square(self, x, y, grid=None):
        assert(x < self._w)
        assert(y < self._h)

        #for testing purposes.  See reset_world_test
        if grid == None:
            grid = self._grid
        return grid[y][x]

    def reset_world(self):
        self._grid = copy.deepcopy(self._original_grid)


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
            D['north'] = (x, y-1)
        if y < (self._h - 1):
            D['south'] = (x, y+1)
        return D

    def pick_up(self, x, y):
        self.get_square(x, y).pick_up()

    def drop_off(self, x, y):
        self.get_square(x, y).drop_off()

    def get_width(self):
        return self._w

    def get_height(self):
        return self._h

###############################################################################
#   Private Functions
###############################################################################

    def _set_locations(self, locations, location_type):
        assert(isinstance(locations, list) or isinstance(locations, tuple))
        assert(locations[-1] is None or isinstance(locations[-1], list)
               or isinstance(locations[-1], tuple))

        for (x, y, n) in locations:
            self._set_location(x, y, n, location_type)

    def _set_location(self, x, y, n, location_type):
        assert(location_type in [PICKUP, DROPOFF])

        if location_type == PICKUP:
            self._grid[y][x] = PickUpLocation(self._pick_up_reward, self._reward, n)
        elif location_type == DROPOFF:
            self._grid[y][x] = DropOffLocation(self._drop_off_reward, self._reward, n)



