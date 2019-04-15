from world import World
from agent import Agent
from functions import q_learning
from policies import p_random, p_greedy, p_exploit
from manager import manager


from copy import deepcopy
def main():
    w = World(5, 5, [(0, 0, 5), (2, 2, 5), (4, 4, 5)],
              [(0, 4, 5), (2, 4, 5), (0, 2, 5)], -1, 15, 15)
    a = Agent(1, 1)


    # This should run experiment number 1.  8000 steps total, the first 4000
    # steps we use PRANDOM policy, then we use PGREEDY for the next 4000 steps
    manager(deepcopy(w), deepcopy(a), q_learning, 0.3, 0.5, p_random, 8000,
            [(4000, p_greedy)])

    manager(deepcopy(w), deepcopy(a), q_learning, 0.3, 0.5, p_random, 8000,
            [(200, p_exploit)])

    #manager(deepcopy(w), deepcopy(a), SARSA, 0.3, 0.5, p_random, 8000,
    #        [(200, p_exploit)])

    #manager(deepcopy(w), deepcopy(a), SARSA, 0.3, 1.0, p_random, 8000,
    #        [(200, p_exploit)])

    #TODO: Add support for manager to swap after 2 iterations of terminal
    #manager(deepcopy(w), deepcopy(a), q_learning, 0.3, 0.5, p_random, 8000,
    #        [(200, p_exploit)])

 


    #manager(deepcopy(w), deepcopy(a), q_learning, 0.3, 0.5, p_random, 8000)
    #manager(deepcopy(w), deepcopy(a), q_learning, 0.3, 0.5, p_greedy, 8000)
    #manager(deepcopy(w), deepcopy(a), q_learning, 0.3, 0.5, p_exploit, 8000)
    #manager(w, a, q_learning, 1.3, 0.5, PRANDOM, 8000, [(4000, PGREEDY)])

if __name__ == '__main__':
    #TODO: Add argument parsing to pass into the main function
    main()

