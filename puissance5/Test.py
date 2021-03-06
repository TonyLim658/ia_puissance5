from puissance5.Puissance import _get_index_token_positionable
from .Puissance import *


def test_array_tuple_manipulation():
    assert ((tuple_to_array((1, 0, -1, 0), 2, 2) == [[1, 0], [-1, 0]]).all())
    assert ((tuple_to_array((1, 0, -1, 0, 1, 1), 3, 2) == [[1, 0, -1], [0, 1, 1]]).all())
    assert ((tuple_to_array(TUPLE_ORIGINAL) == [[EMPTY_CELL for _ in range(BOARD_LENGTH)] for _ in range(BOARD_HEIGHT)]).all())

    assert (array_to_tuple([[1, 0], [-1, 0]]) == (1, 0, -1, 0))
    assert (array_to_tuple([[1, 0, -1], [0, 1, 1]]) == (1, 0, -1, 0, 1, 1))

    assert (_get_index_token_positionable(BOARD_ORIGINAL) == [84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95])
    assert (_get_index_token_positionable(np.array(
                        [[EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [RED_TOKEN,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, YELLOW_TOKEN, EMPTY_CELL, EMPTY_CELL],
                         [RED_TOKEN,  EMPTY_CELL, YELLOW_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, YELLOW_TOKEN, EMPTY_CELL, RED_TOKEN, RED_TOKEN, EMPTY_CELL, EMPTY_CELL]]
                 )) == [60, 85, 74, 87, 88, 89, 78, 91, 80, 69, 94, 95])


def test_check_state():
    assert (check_state(np.array(
                        [[EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [RED_TOKEN,  RED_TOKEN, RED_TOKEN, RED_TOKEN, RED_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]]
                                    )) == RED_TOKEN)

    assert (check_state(np.array(
                        [[EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [RED_TOKEN,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [RED_TOKEN,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [RED_TOKEN,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [RED_TOKEN,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [RED_TOKEN,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]]
                                    )) == RED_TOKEN)

    assert (check_state(np.array(
                        [[EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, RED_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, RED_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, RED_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, RED_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, RED_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]]
                                    )) == RED_TOKEN)

    assert (check_state(np.array(
                        [[RED_TOKEN,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  RED_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, RED_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, RED_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, RED_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]]
                                    )) == RED_TOKEN)

    assert (check_state(np.array(
                        [[EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [RED_TOKEN,  RED_TOKEN, RED_TOKEN, RED_TOKEN, RED_TOKEN, RED_TOKEN, RED_TOKEN, RED_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]]
                                    )) == RED_TOKEN)

    assert (check_state(np.array(
                        [[EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [RED_TOKEN,  RED_TOKEN, RED_TOKEN, RED_TOKEN, RED_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [RED_TOKEN,  YELLOW_TOKEN, RED_TOKEN, RED_TOKEN, YELLOW_TOKEN, RED_TOKEN, RED_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]]
                                    )) == RED_TOKEN)

    assert (check_state(np.array(
                        [[EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [RED_TOKEN,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  RED_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, RED_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, RED_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, RED_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]]
                                    )) == RED_TOKEN)

    assert (check_state(BOARD_ORIGINAL) == UNFINISHED_STATE)

    assert (check_state(np.array(
                        [[RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN],
                         [RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN],
                         [YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN],
                         [YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN],
                         [RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN],
                         [RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN],
                         [YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN],
                         [YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN,    YELLOW_TOKEN, RED_TOKEN]]
                                    )) == EMPTY_CELL)

    assert (check_state(np.array(
                        [[EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [RED_TOKEN,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]]
                                    )) == UNFINISHED_STATE)


def test_heuristic():
    gen_score()
    assert (heuristic(np.array(
                        [[EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [RED_TOKEN,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]]
                                    )) == 0.1)

    assert (heuristic(np.array(
                        [[EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [YELLOW_TOKEN,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]]
                                    )) == -0.1)

    assert (heuristic(np.array(
                        [[EMPTY_CELL,  EMPTY_CELL, RED_TOKEN, EMPTY_CELL, RED_TOKEN, EMPTY_CELL, RED_TOKEN, YELLOW_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, RED_TOKEN, EMPTY_CELL, EMPTY_CELL, YELLOW_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  RED_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, YELLOW_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [RED_TOKEN,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, YELLOW_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]]
                                    )) == 0.3)

    assert (heuristic(np.array(
                        [[EMPTY_CELL,  EMPTY_CELL, RED_TOKEN, EMPTY_CELL, RED_TOKEN, EMPTY_CELL, RED_TOKEN, YELLOW_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, RED_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  RED_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [RED_TOKEN,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]]
                                    )) > 0.7)

    assert (heuristic(np.array(
                        [[EMPTY_CELL,  EMPTY_CELL, YELLOW_TOKEN, EMPTY_CELL, YELLOW_TOKEN, EMPTY_CELL, YELLOW_TOKEN, RED_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  EMPTY_CELL, YELLOW_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [EMPTY_CELL,  YELLOW_TOKEN, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                         [YELLOW_TOKEN,  EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]]
                                    )) < 0.7)


test_array_tuple_manipulation()
test_check_state()
test_heuristic()
print('tests successful')
