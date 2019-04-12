# Created by: Henry Rodriguez
#
# 3 Policies will be used in the experiments:
#   1. PRANDOM
#   2. PEPLOIT
#   3. PGREEDY
#
# 1. PRANDOM:
#              If pickup and dropoff is applicable, choose this operator, otherwise;
#              choose an applicable operator randomly.
#
#
# 2. PEPLOIT:
#              If pickup and dropoff is applicable, choose this operator; otherwise,
#              apply the applicable operator with the highest Q-VALUE (break ties by
#              rolling a dice for operators with the same Q-VALUE) with probability 0.8
#              and choose a different applicable operator with probability 0.2.
#
#
# 3. PGREEDY:
#              If pickup and dropoff is applicable, choose this operator; otherwise,
#              apply the applicable operator with the highest Q-VALUE (break ties by
#              rolling a dice for operators with the same Q-VALUE).
#
#  GRID:
#       Pickup Cells: {(1,1),(3,3),(5,5)}
#       Dropoff Cells: {(1,5),(2,5),(3,5)}
#
#
#

# Libraries imported
import itertools
import random
# Classes imported
from src import agent, world, qtable


class policy:
    # TODO: Create Dice function
    # Need to get Agents poition from Agent.py to compare with pickup/dropoff location tuple
    agentLocal = list(agent.get_Position());  # Returns a tuple containing x,y

    # Assume it's being returned as tuple
    worldDropOffLocal = list(world.drop_off_locations);
    worldPickUpLocal = list(world.pick_up_locations);

    # Delete every 3rd element since reward is not relevant to this class.
    # Assuming tuple (x, y, reward) as seen in world.py
    del worldPickUpLocal[2::3]
    del worldDropOffLocal[2::3]

    # Using list comprehensions
    comparisonsPickUp = [a == b for (a, b) in itertools.product(agentLocal, worldPickUpLocal)]
    comparisonsDropOff = [a == b for (a, b) in itertools.product(agentLocal, worldDropOffLocal)]

    # Flag variable for both pick up and dropoff
    flagPickUp = False
    flagDropOff = False

    if True in comparisonsPickUp:
        flagPickUp = True
    if True in comparisonsDropOff:
        flagDropOff = True


moves = ['North', 'East', 'South', 'West']


def PRANDOM(flagPickUp, flagDropOff):
    if (flagPickUp & flagDropOff == False):
        return random.choice(moves)
    else:
        if (flagPickUp == True):
            return flagPickUp
        if (flagDropOff == True):
            return flagDropOff \
                # Retain highest Q-Value, break ties with dice


def PEPLOIT(flagPickUp, flagDropOff):
    if (flagPickUp == True):
        return flagPickUp
    if (flagDropOff == True):
        return flagDropOff
    ## Psudeo until questions are cleared


#  maxQ = max(Qtable[])
# comparisonsPickUp = [a == b for (a, b) in itertools.product(maxQ, Qtable[])]
# if (tie):
#   tieBreaker = str(random.randint(1, 6))
# TODO: Finish after clarifying with team

# def PGREEDY(flagPickUp, flagDropOff):
