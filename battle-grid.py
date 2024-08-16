class Grid():
    def __init__(self, rows, cols):
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def is_within_bound(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols

    def is_cell_empty(self, x, y):
        if self.is_within_bound(x, y):
            if self.grid[x][y] is None:
                return True
        return False
        
    def place_troop(self,troop, x, y):
        if self.is_cell_empty(x, y):
            self.grid[x][y] = troop
            troop.position = (x, y)
            return True
        return False

    def remove_troop(self, x, y):
        if self.is_within_bound(x, y):
            self.grid[x][y] = None

    def get_state(self):
        return [[cell if cell else "." for cell in row] for row in self.grid]

    def __str__(self):
        return "\n".join([" ".join([str(cell) if cell else "." for cell in row]) for row in self.grid])

class Troop():
    def __init__(self, type):
        self.type = type
        self.position = None
        if self.type == "Infantry":
            self.name = "I"
            self.HP = 100
            self.attack = 30
            self.mov_speed = 1
        elif self.type == "Archer":
            self.name = "A"
            self.HP = 50
            self.attack = 15
            self.mov_speed= 3

    def move(self, grid, dir):
        new_pos = tuple(map(sum, zip(self.position, dir)))
        if grid.is_cell_empty(*new_pos) and (abs(dir[0]) + abs(dir[1])) <= self.mov_speed:
            grid.remove_troop(*self.position)
            grid.place_troop(self, *new_pos)
        
    def __str__(self):
        return self.name

# grid = Grid(5, 5)
# infantry = Troop("Infantry")
# archer = Troop("Archer")
# grid.place_troop(infantry, 0, 1)
# grid.place_troop(archer, 3, 1)
# print(grid)
# archer.move(grid, (1, 2))

# print()
# print(grid)

# grid = Grid(10, 10)
# print(grid)
# print("\n\n\n\n")
# infantry = []
# for _ in range(5):
#     infantry.append(Troop("Infantry"))

# tmp = 0
# for soldier in infantry:
#     grid.place_troop(soldier, 1, tmp)
#     tmp += 1

# print(grid)

# import os
# import time
# os.system("clear")
# print(grid)
# i1 = Troop("Archer")
# grid.place_troop(i1, 5, 3)
# for i in range(10):
#     for soldier in infantry:
#         soldier.move(grid, (1, 0))
#     time.sleep(1)
#     os.system('clear')
#     print(grid)
    
