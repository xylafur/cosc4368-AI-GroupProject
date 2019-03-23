"""
    There is still alot that needs to be done for this module!
"""

class QTable:
    def __init__(self, width, height):
        self._table = {}
        for b in [True, False]:
            for w in range(width):
                for h in range(height):
                    self._table[(w, h, b)] = {}
        self._w = width
        self._h = height

    def update_table(self, x, y, b, vals):
        """
            Vals is expected to be a dict with keys north, south east and west,
            up to two of these can be missing at a time (corner blocks)
        """
        self._table[(x, y, b)] = vals.copy()

    def __repr__(self):
        s = 'x  y  holding block'
        for b in [True, False]:
            for w in range(self._w):
                for h in range(self._h):
                    s += '{} {} {}    '.format(w, h, b) + str(self._table[(w, h, b)]) + '\n'
        return s


