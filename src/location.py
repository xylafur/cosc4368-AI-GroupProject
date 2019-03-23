#!/usr/bin/env python3

"""
    This module contains the implementation of the various type of squares that
    can populate our grid world

    That includes individual squares (locations) of all 3 types (pick up,
    drop off and normal locations)
"""

PICKUP  = "PICKUP"
DROPOFF = "DROPOFF"
NORMAL  = "NORMAL"

class Location:
    """
        This class represents an individual square in our grid world.
    """
    def __init__(self, _type, reward):
        self._type = _type
        self._reward = reward

    def __repr__(self):
        return "{} Location".format(self._type)

    def get_reward(self, has_block):
        return self._reward

    def get_type(self):
        return self._type

    def is_pickup(self):
        return self._type == PICKUP

    def is_dropoff(self):
        return self._type == DROPOFF

class PickUpLocation(Location):
    def __init__(self, pick_up_reward, reward, num_blocks):
        super().__init__(PICKUP, reward)
        self._pur = pick_up_reward
        self._nb = num_blocks

    def check_pick_up(self):
        """
            Returns true if a block can be picked up from this location, False
            otherwise
        """
        return self._nb > 0

    def get_reward(self, has_block):
        """
            Returns the reward for this location.

            Parameters:
                has_block (bool) - Is the agent carrying a block right now?

        """
        # if we can pick up a block here, we assume that the agent will pick up
        # the block, so we return the pick up reward
        if not has_block and self.check_pick_up():
            return self._pur

        return super().get_reward(has_block)

    def pick_up(self):
        """
            Pick up a block from this location.  It is up to the agent to
            record that it is holding the block, this fucntion just decrements
            the number of blocks it currently has
        """
        assert(self.check_pick_up())
        self._nb -= 1

class DropOffLocation(Location):
    def __init__(self, drop_off_reward, reward, capacity):
        super().__init__(DROPOFF, reward)
        self._dor = drop_off_reward
        self._cap = capacity
        self._cur = 0

    def check_drop_off(self):
        """
            Returns true if a block can be dropped off onto this location,
            False otherwise
        """
        return self._cur < self._cap

    def get_reward(self, has_block):
        """
            Returns the reward for this location.

            Parameters:
                has_block (bool) - Is the agent carrying a block right now?

        """
        if has_block and self.check_drop_off():
            return self._pur

        return super().get_reward(has_block)


    def drop_off(self):
        assert(self.check_drop_off())
        self._cur += 1

class NormalLocation(Location):
    def __init__(self, reward):
        super().__init__(NORMAL, reward)
