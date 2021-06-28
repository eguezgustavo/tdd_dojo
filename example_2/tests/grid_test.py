from game.grid import Grid

seed = [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ]

seed_next_generation = [
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 1]
    ]


def test__Grid_class__seed_should_be_saved__when_the_class_is_instantiated():
    grid = Grid(seed)

    assert grid.seed == seed 


def test__calculate_neighbors_method__return_live_neighbors__given_location():
    grid = Grid(seed)

    neighbors = grid.calculate_neighbors([1, 1])

    assert neighbors == 4


def test__calculate_neighbors_method__return_live_neighbors__given_location_on_the_edge():
    grid = Grid(seed)

    neighbors = grid.calculate_neighbors([0, 0])

    assert neighbors == 3


def test__calculate_next_gen_method__return_the_next_generation__when_a_seed_is_given():
    grid = Grid(seed)
    
    grid.calculate_next_gen()

    assert grid.seed == seed_next_generation
    