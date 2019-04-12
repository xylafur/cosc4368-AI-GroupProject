"""
    There is still alot that needs to be done for this module!
"""

from qtable import QTable
from location import PICKUP, DROPOFF

def manager(world, agent, learning_function, learning_rate, discount_rate,
            policy, num_steps, setup=None):
    """
        This function is kinda like the main, it will run the given
        learning_function on the given world with the given learning rate,
        discount rate and policy

        Parameters:
            world (World)
                An instance of a World Object representing the world

            agent (Agent):
                An instance of a Agent Object representing the agent

            learning_function (function):
                A fuinction to call with the world, agent, qtable, learning
                rate, discount rate and policy as parameters that will decide
                where the agent should move and also update the qtable

            learning_rate (float)

            discount_rate (float)

            policy (function)
                The function for the given policy

            num_steps (int)
                how many steps to run for

            setup (list of tuples)
                this is an optional parameter

                it represents different policies that should be activated after
                a particular number of steps

                if this parameter is supplied to the function, it is expected
                to be a list of tupes, where each of the tuples is expected to
                be of this format:
                    (integer, function)

                where the integer is the number of steps, and function is the
                policy to switch to after that many steps have been ran
    """
    if not setup:
        setup = []

    q = QTable(world._w, world._h)
    current_step = 0

    # Set this to None here for the SARSA algorithm.  We won't be 
    action = None
    next_action = None

    while current_step < num_steps:

        # The policy will tell us what our next action will be
        #
        # We have to also compute the next action because SARSA requires this
        # information.  We just return a new agent object that has pretended to
        # move for the first action to the policy function.
        #
        #   There is probably better way of doing this
        if not action:
            action = policy(agent, world)
            next_action = policy(agent.pretend_move(action), world)
        else:
            action = next_action
            next_action = policy(agent.pretend_move(action), world)


        #   Update the q table based on the state we are in and the action we
        #   have chosen
        function(world, agent, q, action, next_action, learning_rate, discount_rate)

        # If we are on a pick up and don't have a block, pick it up.  If we are
        # on a drop off and have a block, drop it off
        pickup_dropoff(world, agent)

        # Move to our new location based on our action
        agent.move(action)

        current_step += 1

        policy = get_new_policy(setup, current_step, policy)

def pickup_dropoff(world, agent):
    # If the agent is on a pick up square that has blocks that can be picked up
    # and the agent is not carrying a block, then pick it up
    if world.is_pickup(*agent.get_pos()) and                                \
            world.check_pick_up(*agent.get_pos()) and                       \
            not agent.is_holding_block():
        world.pick_up(*agent.get_pos())
        agent.pick_up()
    # If the agent is on a drop off square and that square is not full and the
    # agent has a block to drop off, then drop off the block
    elif world.is_drop_off(*agent.get_pos()) and                            \
            world.check_drop_off(*agent.get_pos()) and                      \
            agent.is_holding_block():
        world.drop_off(*agent.get_pos())
        agent.drop_off()




def get_new_policy(setup, steps, current):
    """
        This function will consider the list of tuples 'setup' and the current
        step count 'steps' and return the correct policy from the list of
        tuples.

        Parameters:
            setup (list of tuples)
                it represents different policies that should be activated after
                a particular number of steps

                each of the tuples is expected to be of this format:
                    (integer, function)

                where the integer is the number of steps, and function is the
                policy to switch to after that many steps have been ran

            steps (integer):
                The current number of steps that the simulation has run through
    """
    current_max = 0
    new_policy = None
    for (_steps, policy) in setup:
        if steps >= _steps and _steps > current_max:
            current_max = _steps
            new_policy = policy

    if not new_policy:
        new_policy = current

    return new_policy


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
