class Agent:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._pos = (x, y)
        self._starting_position = (x, y)
        self._holding_block = False

    def get_starting_position(self):
        return self._starting_position

    def move(self, direction):
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

    def is_holding_block(self):
        return self._holding_block

    def pick_up(self):
        assert(not self.is_holding_block())
        self._holding_block = True

    def drop_off(self):
        assert(self.is_holding_block())
        self._holding_block = False

