"""
    There is still alot that needs to be done for this module!
"""

from qtable import QTable

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
