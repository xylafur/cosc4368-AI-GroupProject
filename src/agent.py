from copy import deepcopy
class Agent:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._pos = (x, y)
        self._starting_position = (x, y)
        self._holding_block = False

###############################################################################
#   Public Functions
###############################################################################

    def move(self, direction):
        """
            Move either north, south, east or west

            This does not take in to account the size of the world, so it is
            up to the caller to ensure that the agent is not moving outside the
            world

            Updates both self._x and self._y as well as self._pos


        """
        assert(isinstance(direction, str))
        direction = direction.lower()

        assert(direction in ['north', 'south', 'east', 'west'])
        if direction == 'north':
            self._y -= 1
        elif direction == 'south':
            self._y += 1
        elif direction == 'west':
            self._x -= 1
        else:
            self._x += 1
        self._pos = (self._x, self._y)

    def pretend_move(self, action):
        """
            Makes a copy of this agent.  Makes that agent preform the action
            that is provided and then returns that agent after it has made the
            move.
        """
        _copy = deepcopy(self)
        _copy.move(action)
        return _copy

    def get_position(self):
        """
            returns a tuple containing x and y position
        """
        return self._pos

    def reset_to_start(self):
        self._set_position(*self._starting_position)
        self._holding_block = False

    def is_holding_block(self):
        return self._holding_block

    def pick_up(self):
        assert(not self.is_holding_block())
        self._holding_block = True

    def drop_off(self):
        assert(self.is_holding_block())
        self._holding_block = False

###############################################################################
#   Private Functions
###############################################################################
    def _set_position(self, x, y):
        self._x = x
        self._y = y
        self._pos = (self._x, self._y)
