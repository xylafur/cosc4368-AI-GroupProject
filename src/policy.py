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

    # These will be used to reference the keys using values of the dictionary.
    neigh_keys = list(neighbors_sq.keys())
    neigh_vals = list(neighbors_sq.values())

    # is_pickup_local/is_dropoff_local will be passed to the policy functions
    # as a parameter
    is_pickup_local = ()
    is_dropoff_local = ()

    # normalSq  - will contain (x,y) all the normal square neighbors relative to agent.
    normalSq = []  # Not sure if needed.
    for posit in neigh_vals():
        is_pickup = world.is_pick(posit[0], posit[1])
        is_dropoff = world.is_dropoff(posit[0], posit[1])
        if (is_pickup == True):
            is_pickup_local = (posit[0], posit[1])
        if (is_dropoff_local == True):
            is_dropoff_local = (posit[0], posit[1])
        else:
            normalSq.append(posit[0], posit[1])

    def PRANDOM(self, is_pickup_local, is_dropoff_local, neigh_keys, neigh_vals):
        # TODO: REFACTOR THESE CONDITIONAL STATEMENTS
        if (len(is_pickup_local) != 0):
            print(neigh_keys[neigh_vals.index(is_pickup_local)])
            return neigh_keys[neigh_vals.index(is_pickup_local)]
        else:
            if (len(is_dropoff_local) != 0):
                print(neigh_keys[neigh_vals.index(is_pickup_local)])
                return neigh_keys[neigh_vals.index(is_dropoff_local)]
            else:
                # Return random selection of available direction
                print(random.choice(neigh_keys))
                return random.choice(neigh_keys)



    def PEPLOIT(self, ):

# Psudeo until questions are cleared. Not sure how y'all are going to want to handle the Q-table
# maxQVal = max(qvals)  # Highest Q-value
        # Check the number of maxQVal there are in qvals
    # how are the qvalues going to be handledd

    #  maxQ = max(Qtable[])
    # comparisonsPickUp = [a == b for (a, b) in itertools.product(maxQ, Qtable[])]
    # if (tie):
    #   tieBreaker = str(random.randint(1, 6))

    # def PGREEDY(flagPickUp, flagDropOff):

    # TODO: Pass to manager.py next move north, east,west, south
