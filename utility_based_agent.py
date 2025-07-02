# Utility-Based Agent Code
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

    def all_clean(self):
        return all(not cell for row in self.grid for cell in row)

    def run(self):
        model = [row[:] for row in self.grid]
        pos = self.agent_pos
        utility = 0
        actions = []

        def find_nearest_dirty(pos):
            queue = [(0, pos, [])]
            visited = set()
            while queue:
                dist, (x, y), path = heapq.heappop(queue)
                if model[x][y]:
                    return path
                visited.add((x, y))
                for d in DIRECTIONS:
                    dx, dy = MOVE[d]
                    nx, ny = x + dx, y + dy
                    if in_bounds(nx, ny) and (nx, ny) not in visited:
                        heapq.heappush(queue, (dist + 1, (nx, ny), path + [d]))
            return []

        while not self.all_clean():
            x, y = self.agent_pos
            if model[x][y]:
                model[x][y] = False
                self.suck()
                utility += 5
                actions.append("suck")
            else:
                path = find_nearest_dirty(self.agent_pos)
                if not path:
                    break
                for direction in path:
                    self.move(direction)
                    actions.append(direction)
                    utility -= 1
                    pos = self.agent_pos

            print_grid(self.grid, self.agent_pos)

        print("Actions taken:", actions)
        print("Total utility:", utility)

if __name__ == "__main__":
    print("Utility-Based Agent")
    env = Environment()
    env.run()
