"""
    This module is to be an implementation for the regular q learning function
    as well as the SARSA q learning function

"""
from manager import get_current_state

##################
#   Right now these are just filled with placeholders
##################
def q_learning(world, agent, qtable, action, next_action, learning_rate, discount_rate):
    # this is a pickup or dropoff.. just return because we don't update the q
    # value for it
    if isinstance(qtable[get_current_state(world, agent)], str):
        return

    # not correct, just for testing
    qtable[get_current_state(world, agent)][action] = \
            world.get_reward(*agent.get_position(), agent.is_holding_block())

def SARSA(world, agent, qtable, action, next_action, learning_rate, discount_rate):
    # this is a pickup or dropoff.. just return because we don't update the q
    # value for it
    if isinstance(qtable[get_current_state(world, agent)], str):
        return

    # not correct, just for testing
    qtable[get_current_state(world, agent)][action] = \
            world.get_reward(*agent.get_position(), agent.is_holding_block())


