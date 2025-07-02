# Goal-Based Agent Code
import random
import heapq

GRID_SIZE = 10
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
        self.model = [row[:] for row in self.grid]
        self.actions = []

    def percept(self):
        x, y = self.agent_pos
        return self.grid[x][y]

    def suck(self):
        x, y = self.agent_pos
        self.grid[x][y] = False
        self.model[x][y] = False
        self.actions.append("suck")

    def move(self, direction):
        dx, dy = MOVE[direction]
        x, y = self.agent_pos
        nx, ny = x + dx, y + dy
        if in_bounds(nx, ny):
            self.agent_pos = (nx, ny)
            self.actions.append(direction)

    def find_nearest_dirty(self):
        queue = [(0, self.agent_pos)]
        visited = set()
        while queue:
            dist, (x, y) = heapq.heappop(queue)
            if self.model[x][y]:
                return (x, y)
            visited.add((x, y))
            for d in DIRECTIONS:
                dx, dy = MOVE[d]
                nx, ny = x + dx, y + dy
                if in_bounds(nx, ny) and (nx, ny) not in visited:
                    heapq.heappush(queue, (dist + 1, (nx, ny)))
        return None

    def all_clean(self):
        return all(not cell for row in self.model for cell in row)

    def move_to_target(self, target):
        tx, ty = target
        while self.agent_pos != target:
            x, y = self.agent_pos
            if x < tx:
                self.move('down')
            elif x > tx:
                self.move('up')
            elif y < ty:
                self.move('right')
            elif y > ty:
                self.move('left')

    def run(self):
        while not self.all_clean():
            if self.percept():
                self.suck()
            else:
                target = self.find_nearest_dirty()
                if not target:
                    break
                self.move_to_target(target)
        print("Final Grid:")
        print_grid(self.grid, self.agent_pos)
        print("Actions:", self.actions)

if __name__ == "__main__":
    print("Goal-Based Agent")
    env = Environment()
    env.run()