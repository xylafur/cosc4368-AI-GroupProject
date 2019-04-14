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
# 80% go with the best choice, and 20% you'll go with the
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
# 10
#
#

# Libraries imported
import itertools
import random
# Classes imported
from src import agent, world, qtable


class policy:
    # Creating objects
    agent = agent();
    world = world();
    qtable = qtable();


    #TODO: Create Dice function

    # Need to get Agents poition from Agent.py to compare with pickup/dropoff location tuple
    agent_local = list(agent.get_Position())  # Returns a tuple containing x,y
    x = agent_local(0)
    y = agent_local(1)

    # Retrive the neighboring squares of the agent
    neighbors_sq = world.get_neighbors()

    # Check if the neighboring locations are pickup locations


for posit in neighbors_sq.values():
    is_pickup = world.is_pick(posit[0], posit[1])
    if (is_pickup == True):




    ## Used to compare the pickup/dropoff locations with neighboring locations
    # TODO: Check if team would be cool with having a function that returns this instead of having it in this class.
    # for ag_lcal in neighbors_sq.values():
    #     print(ag_lcal)
    #     comparisons = [a == b for (a,b) in itertools.product(,[ag_lcal])]
    #     print(comparisons)
    #     if (comparisons == True):
    #


    # TODO: call functions from world.
    # Assume it's being returned as tuple
    # worldDropOffLocal = list(world.drop_off_locations);
    # worldPickUpLocal = list(world.pick_up_locations);




    # Delete every 3rd element since reward is not relevant to this class.
    # Assuming tuple (x, y, reward) as seen in world.py
    del worldPickUpLocal[2::3]
    del worldDropOffLocal[2::3]


# compare to pickup drop off location that is valid, then choose them, or chose random o
## This doesn't actually matter, pick we would rather move to the pick up or drop off locatoion
# # Using list comprehensions
# comparisonsPickUp = [a == b for (a, b) in itertools.product(agentLocal, worldPickUpLocal)]
# comparisonsDropOff = [a == b for (a, b) in itertools.product(agentLocal, worldDropOffLocal)]
#
# # Flag variable for both pick up and dropoff
# flagPickUp = False
# flagDropOff = False
#
# if True in comparisonsPickUp:
#     flagPickUp = True
# if True in comparisonsDropOff:
#     flagDropOff = True


moves = ['North', 'East', 'South', 'West']


def PRANDOM(self, flagPickUp, flagDropOff):
    if (flagPickUp & flagDropOff == False):
        return random.choice(moves)
    else:
        if (flagPickUp == True):
            return flagPickUp
        if (flagDropOff == True):
            return flagDropOff
                # Retain highest Q-Value, break ties with dice


qvals = list(qtable.get_relevant_sqaures());


def PEPLOIT(self, flagPickUp, flagDropOff):
    if (flagPickUp == True):
        return flagPickUp
    if (flagDropOff == True):
        return flagDropOff
    ## Psudeo until questions are cleared. Not sure how y'all are going to want to handle the Q-table
    maxQVal = max(qvals)  # Highest Q-value
    # Check the number of maxQVal there are in qvals
# how are the qvalues going to be handledd


#  maxQ = max(Qtable[])
# comparisonsPickUp = [a == b for (a, b) in itertools.product(maxQ, Qtable[])]
# if (tie):
#   tieBreaker = str(random.randint(1, 6))
# TODO: Finish after clarifying with team

# def PGREEDY(flagPickUp, flagDropOff):


# TODO: Pass to manager.py next move north, east,west, south
