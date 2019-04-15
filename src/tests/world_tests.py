from test import test, TESTS
from world import World


@test
def world_pick_up_drop_off_test():
    w = World(5, 5, [(1, 1, 3), (2, 2, 4)], [(3, 3, 3), (4, 4, 4)], -1, 13, 13)

    assert(w.is_pickup(1, 1))

    assert(w.is_dropoff(4, 4))

    #Make sure that after we pick up all blocks it registers as empty
    w.pick_up(1, 1)
    w.pick_up(1, 1)
    w.pick_up(1, 1)
    assert(not w.is_pickup(1, 1))

    #same thing for drop offs
    w.drop_off(3, 3)
    w.drop_off(3, 3)
    w.drop_off(3, 3)
    assert(not w.is_dropoff(3, 3))

    assert(not w.is_pickup(1, 4))
    assert(not w.is_dropoff(1, 4))

@test
def world_get_reward_test():
    w = World(5, 5, [(1, 1, 3), (2, 2, 4)], [(3, 3, 3), (4, 4, 4)], -1, 13, 13)
    assert(w.get_reward(0, 0, False) == -1)

    assert(w.get_reward(3, 3, False) == -1)
    assert(w.get_reward(3, 3, True) == 13)

    assert(w.get_reward(1, 1, True) == -1)
    assert(w.get_reward(1, 1, False) == 13)

@test
def swap_pickup_dropoff_test():
    w = World(5, 5, [(1, 1, 3), (2, 2, 4)], [(3, 3, 3), (4, 4, 4)], -1, 13, 13)

    for (x, y) in [(1, 1), (2, 2)]:
        assert(w.get_square(x, y).is_pickup())

    for (x, y) in [(3, 3), (4, 4)]:
        assert(w.get_square(x, y).is_dropoff())

    w.swap_pickup_dropoff()

    for (x, y) in [(1, 1), (2, 2)]:
        assert(w.get_square(x, y).is_dropoff())

    for (x, y) in [(3, 3), (4, 4)]:
        assert(w.get_square(x, y).is_pickup())

    w.swap_pickup_dropoff()

    for (x, y) in [(1, 1), (2, 2)]:
        assert(w.get_square(x, y).is_pickup())

    for (x, y) in [(3, 3), (4, 4)]:
        assert(w.get_square(x, y).is_dropoff())


@test
def get_neighbors_test():
    w = World(5, 5, [(1, 1, 3), (2, 2, 4)], [(3, 3, 3), (4, 4, 4)], -1, 13, 13)

    n1 = w.get_neighbors(0, 0)
    assert('south' in n1 and 'east' in n1 and not 'west' in n1 and not 'north' in n1)

    n2 = w.get_neighbors(3, 3)
    assert('south' in n2 and 'east' in n2 and 'west' in n2 and 'north' in n2)

    n3 = w.get_neighbors(4, 4)
    assert(not 'south' in n3 and not 'east' in n3 and 'west' in n3 and 'north' in n3)

@test
def reset_world_test():
    w = World(5, 5, [(1, 1, 3), (2, 2, 4)], [(3, 3, 3), (4, 4, 4)], -1, 13, 13)

    g_o_b_c_1 = w.get_block_count(1, 1, w._original_grid)
    g_o_b_c_3 = w.get_block_count(3, 3, w._original_grid)

    for x in range(5):
        for y in range(5):
            assert(w.get_block_count(x, y, w._original_grid) == w.get_block_count(x, y))

    w.pick_up(1, 1)

    assert(w.get_block_count(1, 1) != g_o_b_c_1)

    w.drop_off(3, 3)

    assert(w.get_block_count(3, 3) != g_o_b_c_3)

    w.reset_world()

    for x in range(5):
        for y in range(5):
            assert(w.get_block_count(x, y, w._original_grid) == w.get_block_count(x, y))
