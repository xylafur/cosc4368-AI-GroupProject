from world import World
from agent import Agent
from functions import q_learning, SARSA, PRANDOM, PEPLOIT, PGREEDY
from manager import manager

def main():
    w = World(5, 5, [(0, 0, 5), (2, 2, 5), (4, 4, 5)],
              [(1, 4, 5), (3, 4, 5), (4, 1, 5)], -1, 15, 15)
    a = Agent(1, 1)

    # This should run experiment number 1.  8000 steps total, the first 4000
    # steps we use PRANDOM policy, then we use PGREEDY for the next 4000 steps
    manager(w, a, q_learning, 0.3, 0.5, PRANDOM, 8000, [(4000, PGREEDY)])

if __name__ == '__main__':
    #TODO: Add argument parsing to pass into the main function
    main()

