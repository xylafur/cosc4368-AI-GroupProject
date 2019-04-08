"""
    There is still alot that needs to be done for this module!
"""

from qtable import QTable
from location import PICKUP, DROPOFF

def manager(world, agent, algo, learning_rate, discount_rate, policy,
            num_steps, setup=None):
    """
        This function is kinda like the main, it will run the given algorithm
        on the given world with the given learning rate, discount rate and
        policy

        Parameters:
            world (World)
                An instance of a World Object representing the world

            agent (Agent):
                An instance of a Agent Object representing the agent

            algo (function):
                A fuinction to call with the world, agent, qtable, learning
                rate, discount rate and policy as parameters that will decide
                where the agent should move and also update the qtable

            learning_rate (float)

            discount_rate (float)

            policy (string)
                PRANDOM, PEPLOIT or PGREEDY

            num_steps (int)
                how many steps to run for

            setup (list of tuples)
                this is an optional parameter

                it represents different policies that should be activated after
                a particular number of steps

                if this parameter is supplied to the function, it is expected
                to be a list of tupes, where each of the tuples is expected to
                be of this format:
                    (integer, string)

                where the integer is the number of steps, and string is the
                policy to switch to after that many steps have been ran
    """
    if not setup:
        setup = []

    q = QTable(world._w, world._h)

def get_current_state(world, agent):
    """
        Returns the state of the universe (as a tuple) based on the agent and
        world states

        The state is of thie format

        (x position of the agent, y position of the agent, is the agent holding
         a block?, status of pickup locations, status of drop off locations)

        the status of the pick up and drop off locations will be multiple
        entries, the number of entries will be equal to the number of pickup
        and dropoff locations.  The status is true if blocks can be picked up
        or dropped off still, but false otherwise.
    """
    x, y = agent.get_position()
    block = agent.is_holding_block()
    pickup_status = world.locations_status(PICKUP)
    dropoff_status = world.locations_status(DROPOFF)

    return (x, y, block, *pickup_status, *dropoff_status)
