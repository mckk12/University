from queue import PriorityQueue
from collections import deque

class Maze:
    def __init__(self, maze_str):
        self.m = []
        self.goals = set()
        self.starts = set()
        self.walls = set()

        for x in maze_str.split('\n'):
            x = x.strip()
            if x:
                self.m.append(list(x))

        for y in range(len(self.m)):
            raw = self.m[y]
            for x in range(len(raw)):
                if self.m[y][x] == 'S':
                    self.starts.add((x, y))
                if self.m[y][x] == 'G':
                    self.goals.add((x, y))
                if self.m[y][x] == 'B':
                    self.starts.add((x, y))
                    self.goals.add((x, y))
                if self.m[y][x] == '#':
                    self.walls.add((x, y))

class A_star():
    def __init__(self, maze, alpha=0.0):
        self.start_positions = maze.starts
        self.maze = maze
        self.alpha = alpha # do zadania 4

        self.distances = self.precalc_distances()

        self.queue = PriorityQueue()
        # cost, moves_count, positions_count, positions, moves
        self.queue.put((self.heuristic(self.start_positions),  0, self.start_positions, '')) 
        self.visited = {tuple(sorted(self.start_positions))}
        # print(self.distances)

    def precalc_distances(self):
        queue = deque([x, y, 0] for (x, y) in self.maze.goals)
        distances = [[float('inf') for _ in range(len(self.maze.m[0]))] for _ in range(len(self.maze.m))]

        while queue:
            x, y, d = queue.popleft()
            if distances[y][x] != float('inf'):
                continue
            distances[y][x] = d
            
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in self.maze.walls and distances[ny][nx] == float('inf'):
                    queue.append((nx, ny, d + 1))
        return distances


    def heuristic(self, positions):
        return (1 + self.alpha) * max(self.distances[y][x] for (x, y) in positions)
    
    def is_final(self, positions):
        for pos in positions:
            if pos not in self.maze.goals:
                return False
        return True
    
    def simulate_move(self, positions, dir):
        new_positions = set()
        for pos in positions:
            dx, dy = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}[dir]
            new_pos = (pos[0] + dx, pos[1] + dy)
            if new_pos not in self.maze.walls:
                new_positions.add(new_pos)
            else:
                new_positions.add(pos)
        return new_positions
      
    def search(self):
        while self.queue.qsize() > 0:
            _, d, curr_pos, curr_moves = self.queue.get()
            # print(len(curr_pos), curr_moves, c)
            if self.is_final(curr_pos):
                return curr_moves
            for move in ['R', 'L', 'U', 'D']:
                new_positions = self.simulate_move(curr_pos, move)
                frozen = tuple(sorted(new_positions))
                if frozen not in self.visited:
                    self.queue.put((self.heuristic(new_positions) + d + 1, d + 1, new_positions, curr_moves + move))
                    self.visited.add(frozen)

        return curr_moves
    

if __name__ == '__main__':
    input_file = "zad_input.txt"
    output_file = "zad_output.txt"
    with open(input_file, 'r') as file:
        maze_str = file.read()
    m = Maze(maze_str)
    a = A_star(m, 0.09)
    answer = a.search()
    # print(answer)
    with open(output_file, 'w') as file:
        file.write(answer)