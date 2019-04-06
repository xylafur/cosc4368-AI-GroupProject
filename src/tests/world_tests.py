from test import test, TESTS
from world import World


@test
def world_pick_up_drop_off_test():
    w = World(5, 5, [(1, 1, 3), (2, 2, 4)], [(3, 3, 3), (4, 4, 4)], -1, 13, 13)

    assert(w.is_pickup(1, 1))
    assert(w.check_pick_up(1, 1))

    assert(w.is_dropoff(4, 4))
    assert(w.check_drop_off(4, 4))

    #Make sure that after we pick up all blocks it registers as empty
    w.pick_up(1, 1)
    w.pick_up(1, 1)
    w.pick_up(1, 1)
    assert(w.is_pickup(1, 1))
    assert(not w.check_pick_up(1, 1))

    #same thing for drop offs
    w.drop_off(3, 3)
    w.drop_off(3, 3)
    w.drop_off(3, 3)
    assert(w.is_dropoff(3, 3))
    assert(not w.check_drop_off(3, 3))


    assert(not w.is_pickup(1, 4))
    assert(not w.is_dropoff(1, 4))


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
