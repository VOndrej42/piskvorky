from piskvorky.handlers.grid import print_grid


def test_print_grid():
    grid_mock = [["_","_","_"],["_","_","_"],["_","_","_"]]
    assert print_grid(grid_mock, 3, 3) == """0 1 2
0 _ _ _
1 _ _ _
2 _ _ _"""