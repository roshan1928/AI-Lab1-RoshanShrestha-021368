# Simple Reflex Agent Code
import random

GRID_SIZE = 10
STEPS = 20
DIRECTIONS = ['up', 'down', 'left', 'right']
MOVE = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

def in_bounds(x, y):
    return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE

def print_grid(grid, agent_pos):
    for i in range(GRID_SIZE):
        row = ''
        for j in range(GRID_SIZE):
            if (i, j) == agent_pos:
                row += 'A '
            elif grid[i][j]:
                row += 'D '
            else:
                row += '. '
        print(row)
    print("-" * 20)

class Environment:
    def __init__(self):
        self.grid = [[random.choice([True, False]) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.agent_pos = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))

    def percept(self):
        x, y = self.agent_pos
        return self.grid[x][y]

    def suck(self):
        x, y = self.agent_pos
        self.grid[x][y] = False

    def move(self, direction):
        dx, dy = MOVE[direction]
        x, y = self.agent_pos
        nx, ny = x + dx, y + dy
        if in_bounds(nx, ny):
            self.agent_pos = (nx, ny)

    def run(self):
        for step in range(STEPS):
            print(f"Step {step+1}")
            if self.percept():
                self.suck()
            else:
                direction = random.choice(DIRECTIONS)
                self.move(direction)
            print_grid(self.grid, self.agent_pos)

if __name__ == "__main__":
    print("Simple Reflex Agent")
    env = Environment()
    env.run()
