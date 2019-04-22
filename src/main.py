from world import World
from agent import Agent
from functions import q_learning, SARSA
from policies import p_random, p_greedy, p_exploit
from manager import manager


from copy import deepcopy
def main():
    w = World(5, 5, [(0, 0, 5), (2, 2, 5), (4, 4, 5)],
              [(0, 4, 5), (2, 4, 5), (0, 2, 5)], -1, 15, 15)
    a = Agent(1, 1)

    manager(deepcopy(w), deepcopy(a), q_learning, 0.3, 0.5, p_random, 8000,
            [(4000, p_greedy)], filename="Experiment1_1.txt")
    manager(deepcopy(w), deepcopy(a), q_learning, 0.3, 0.5, p_random, 8000,
            [(4000, p_greedy)], filename="Experiment1_2.txt")

    manager(deepcopy(w), deepcopy(a), q_learning, 0.3, 0.5, p_random, 8000,
            [(200, p_exploit)], filename="Experiment2_1.txt")
    manager(deepcopy(w), deepcopy(a), q_learning, 0.3, 0.5, p_random, 8000,
            [(200, p_exploit)], filename="Experiment2_2.txt")

    manager(deepcopy(w), deepcopy(a), SARSA, 0.3, 0.5, p_random, 8000,
            [(200, p_exploit)], filename="Experiment3_1.txt")
    manager(deepcopy(w), deepcopy(a), SARSA, 0.3, 0.5, p_random, 8000,
            [(200, p_exploit)], filename="Experiment3_2.txt")

    manager(deepcopy(w), deepcopy(a), SARSA, 0.3, 1.0, p_random, 8000,
            [(200, p_exploit)], filename="Experiment4_1.txt")
    manager(deepcopy(w), deepcopy(a), SARSA, 0.3, 1.0, p_random, 8000,
            [(200, p_exploit)], filename="Experiment4_2.txt")
    manager(deepcopy(w), deepcopy(a), q_learning, 0.3, 0.5, p_random, 8000,
            [(200, p_exploit)], swap_after_iter=2, filename="Experiment5_1.txt")
    manager(deepcopy(w), deepcopy(a), q_learning, 0.3, 0.5, p_random, 8000,
            [(200, p_exploit)], swap_after_iter=2, filename="Experiment5_2.txt")


    manager(deepcopy(w), deepcopy(a), q_learning, 0.3, 0.5, p_random, 8000,
            [(4000, p_greedy)], filename="Experiment1_SmallStatespace_1.txt",
            state_space='small')
    manager(deepcopy(w), deepcopy(a), q_learning, 0.3, 0.5, p_random, 8000,
            [(4000, p_greedy)], filename="Experiment1_SmallStatespace_2.txt",
            state_space='small')

    manager(deepcopy(w), deepcopy(a), q_learning, 0.3, 0.5, p_random, 8000,
            [(200, p_exploit)], filename="Experiment2_SmallStatespace_1.txt",
            state_space='small')
    manager(deepcopy(w), deepcopy(a), q_learning, 0.3, 0.5, p_random, 8000,
            [(200, p_exploit)], filename="Experiment2_SmallStatespace_2.txt",
            state_space='small')

    manager(deepcopy(w), deepcopy(a), SARSA, 0.3, 0.5, p_random, 8000,
            [(200, p_exploit)], filename="Experiment3_SmallStatespace_1.txt",
            state_space='small')
    manager(deepcopy(w), deepcopy(a), SARSA, 0.3, 0.5, p_random, 8000,
            [(200, p_exploit)], filename="Experiment3_SmallStatespace_2.txt",
            state_space='small')

    manager(deepcopy(w), deepcopy(a), SARSA, 0.3, 1.0, p_random, 8000,
            [(200, p_exploit)], filename="Experiment4_SmallStatespace_1.txt",
            state_space='small')
    manager(deepcopy(w), deepcopy(a), SARSA, 0.3, 1.0, p_random, 8000,
            [(200, p_exploit)], filename="Experiment4_SmallStatespace_2.txt",
            state_space='small')

    manager(deepcopy(w), deepcopy(a), q_learning, 0.3, 0.5, p_random, 8000,
            [(200, p_exploit)], swap_after_iter=2,
            filename="Experiment5_SmallStatespace_1.txt",
            state_space='small')
    manager(deepcopy(w), deepcopy(a), q_learning, 0.3, 0.5, p_random, 8000,
            [(200, p_exploit)], swap_after_iter=2,
            filename="Experiment5_SmallStatespace_2.txt",
            state_space='small')

if __name__ == '__main__':
    #TODO: Add argument parsing to pass into the main function
    main()

