"""
    These modules should return the next action that should be taken given the
    current state of the agent and the positions around the agent in the world.
"""

PRANDOM = "PRANDOM"
PEPLOIT = "PEPLOIT"
PGREEDY = "PGREEDY"

##################
#   I have no idea what these functions will actually need, this is up to the
#   implementer.  They can be changed based on what the designer requires
##################
def p_random(agent, world):
    raise NotImplementedError()

def p_greedy(agent, world):
    raise NotImplementedError()

def p_exploit(agent, world):
    raise NotImplementedError()
