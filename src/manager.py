"""
    There is still alot that needs to be done for this module!
"""

import os

from location import PICKUP, DROPOFF
from qtable import QTable

OUT_DIR="ExperimentOutput"

def write_experiment_output(directory, filename, world, agent, qtable, policy,
                            iteration, movements, heatmap, state_space,
                            steps_per_iter):
    if not os.path.isdir(directory):
        os.mkdir(directory)
    # only doing this because I know it will work on any platform.. the whole
    # slash thing sucks
    orgdir = os.getcwd()
    os.chdir(directory)

    with open(filename, 'w') as f:
        f.write(filename + '\r\n')
        f.write("Current State: {}\r\n".format(get_current_state(
            world, agent, state_space=state_space)))
        f.write("Ending Policy: {}\r\n\r\n".format(policy.__name__))

        f.write("Total Moves: {}\r\n".format(agent._total_moves))
        f.write("Total Iterations: {}\r\n".format(iteration))
        f.write("Total Pickups: {}\r\n".format(agent._total_pickups))
        f.write("Total Dropoffs: {}\r\n\r\n".format(agent._total_dropoffs))

        f.write("Starting Pick Up Locations: {}\r\n".format(world._org_pick_up_locations))
        f.write("Starting Drop Off Locations: {}\r\n".format(world._org_drop_off_locations))
        f.write("Ending Pick Up Locations: {}\r\n".format(world._pick_up_locations))
        f.write("Ending Drop OffLocations: {}\r\n\r\n".format(world._drop_off_locations))

        f.write("Steps per each iteration\r\n")
        for ii, steps in enumerate(steps_per_iter):
            f.write("Iteration: {}, Steps: {}\r\n".format(ii + 1, steps))
        f.write("\r\n")

        f.write("Percent of states visited: {}\r\n\r\n".format(
            qtable.percent_visited()))

        f.write("Heatmap of visited locations:\r\n")

        tot_sum = 0
        for col in heatmap:
            f.write("    " + " ".join([str(row) for row in col]))
            f.write("\r\n")
            tot_sum += sum(col)

        #just sanity checking because the numbers seem weird...
        assert(tot_sum == 8000)

        f.write("\r\nMovements over time for the agent: \r\n")
        f.write("\r\n\tMovement#\tPosition\tBlocks?\r\n")
        for ii, each in enumerate(movements):
            f.write("\t{}\t\t\t{}\t\t\t{}\r\n".format(ii, each[0], each[1]))
        f.write("\r\n")

        f.write("Resulting Q Table\r\n")
        f.write(qtable.__repr__())

    os.chdir(orgdir)

def manager(world, agent, learning_function, learning_rate, discount_rate,
            policy, num_steps, setup=None, swap_after_iter=None,
            filename="give_me_a_name.txt", state_space='big'):
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

    q = QTable(world, state_space=state_space)
    current_step = 0

    # Set this to None here for the SARSA algorithm.  We won't be 
    action = None
    next_action = None
    iteration = 1

    movements = []

    steps_this_iter = 0
    steps_per_iter = []

    heatmap = [[0 for _ in range(world._w)] for __ in range(world._h)]
    swapped = False

    while current_step < num_steps:
        movements.append((agent.get_position(), agent.is_holding_block()))
        heatmap[agent.get_position()[1]][agent.get_position()[0]] += 1

        if is_world_solved(world, agent):
            world.reset_world()
            agent.reset_to_start()
            iteration += 1

            steps_per_iter.append(steps_this_iter)
            steps_this_iter = 0

        steps_this_iter += 1

        if swap_after_iter and (swap_after_iter + 1) == iteration and not swapped:
            world.swap_pickup_dropoff()
            swapped = True


        # The policy will tell us what our next action will be
        #
        # We have to also compute the next action because SARSA requires this
        # information.  We just return a new agent object that has pretended to
        # move for the first action to the policy function.
        #
        #   There is probably better way of doing this
        if not action:
            action = policy(agent, world, q, state_space=state_space)
            next_action = policy(agent.pretend_move(action), world, q,
                                 state_space=state_space)
        else:
            action = next_action
            next_action = policy(agent.pretend_move(action), world, q,
                                 state_space=state_space)


        #   Update the q table based on the state we are in and the action we
        #   have chosen
        learning_function(world, agent, q, action, next_action, learning_rate,
                          discount_rate, state_space=state_space)

        # If we are on a pick up and don't have a block, pick it up.  If we are
        # on a drop off and have a block, drop it off
        pickup_dropoff(world, agent)

        # Move to our new location based on our action
        agent.move(action)

        current_step += 1

        policy = get_new_policy(setup, current_step, policy)

    write_experiment_output(OUT_DIR, filename, world, agent, q, policy,
                            iteration, movements, heatmap, state_space,
                            steps_per_iter)

is_world_solved = lambda world, agent: world.is_world_solved()

def pickup_dropoff(world, agent):
    # If the agent is on a pick up square that has blocks that can be picked up
    # and the agent is not carrying a block, then pick it up
    if world.is_pickup(*agent.get_position()) and not agent.is_holding_block():
        world.pick_up(*agent.get_position())
        agent.pick_up()
    # If the agent is on a drop off square and that square is not full and the
    # agent has a block to drop off, then drop off the block
    elif world.is_dropoff(*agent.get_position()) and agent.is_holding_block():
        world.drop_off(*agent.get_position())
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

def get_current_state(world, agent, state_space='big'):
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

    if state_space != 'big':
        return (x, y, block)

    pickup_status = world.locations_status(PICKUP)
    dropoff_status = world.locations_status(DROPOFF)

    return (x, y, block, *pickup_status, *dropoff_status)
