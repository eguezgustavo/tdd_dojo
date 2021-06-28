from .cell import Cell


class Grid:

    def __init__(self, seed):
        self.seed = seed
    
    def calculate_neighbors(self, location):
        location_in_x = location[0]
        location_in_y = location[1]

        neighbors = 0 - self.seed[location_in_y][location_in_x]

        for neighbor_in_y in [-1, 0, 1]: 
            for neighbor_in_x in [-1, 0, 1]:
                neighbor_location_x = location_in_x + neighbor_in_x
                neighbor_location_y = location_in_y + neighbor_in_y
                
                if neighbor_location_y in range(len(self.seed)) and neighbor_location_x in range(len(self.seed[0])):
                    is_neighbor_alive = self.seed[neighbor_location_y][neighbor_location_x]
                else:
                    is_neighbor_alive = 0
                neighbors += is_neighbor_alive

        return neighbors

    def calculate_next_gen(self):
        next_gen = []
        for location_in_y in range(len(self.seed)):
            next_gen_y = []
            for location_in_x in range(len(self.seed[0])):
                cell = Cell(self.seed[location_in_y][location_in_x])
                neighbors = self.calculate_neighbors([location_in_x, location_in_y])
                cell.update_state(neighbors)
                next_gen_y.append(cell.state)
            next_gen.append(next_gen_y)
        self.seed = next_gen
