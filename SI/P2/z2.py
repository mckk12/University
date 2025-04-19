import random as rd
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

class State:
    def __init__(self, maze, positions, moves):
        self.maze = maze
        self.positions = positions
        self.moves = moves

    # jest w stanie zaakceptowac 2 stany do zakonczenia gry w wymaganym czasie 
    def reduce(self, threshold = 2):
        dirs = ['R', 'L', 'D', 'U']       
        
        lowest = len(self.positions) + 1
        low_pos = self.positions
        low_moves = ''
        visited = set()
        visited.add(frozenset(self.positions))

        for _ in range(400):
            moves = ''
            new_positions = self.positions
            generate_moves = [rd.choice(dirs)*5 for _ in range(24)]
            generate_moves = "".join(generate_moves)
            for move in generate_moves:
                new_positions = self.simulate_move(new_positions, move, self.maze)
                moves += move

                if frozenset(new_positions) in visited:
                    continue
                visited.add(frozenset(new_positions))

                if len(new_positions) < lowest or (len(new_positions) == lowest and len(moves) < len(low_moves)):
                    lowest = len(new_positions)
                    low_pos = new_positions
                    low_moves = moves
            if lowest <= threshold:
                break

            
        self.positions = low_pos
        self.moves += low_moves

        # print(len(self.positions))

    def simulate_move(self, positions, dir, maze):
        new_positions = set()
        for position in positions:
            new_pos = self.move(position, dir)
            if new_pos not in maze.walls:
                new_positions.add(new_pos)
            else:
                new_positions.add(position)
        return new_positions

    def move(self, position, dir):
        dirrections = {'U':(0, -1), 'D':(0, 1), 'L':(-1, 0), 'R':(1, 0)}
        return (position[0] + dirrections[dir][0], position[1] + dirrections[dir][1])
    
class BFS:
    def __init__(self, start_state):
        self.start_state = start_state
        self.queue = deque([start_state])
        self.visited = set()
        self.visited.add(frozenset(start_state.positions))

    def is_final(self, state):
        for pos in state.positions:
            if pos not in self.start_state.maze.goals:
                return False
        return True
    
    def search(self):
        while len(self.queue) > 0:
            actual_state = self.queue.popleft()
            if self.is_final(actual_state):
                return actual_state
            for move in ['R', 'L', 'U', 'D']:
                new_positions = actual_state.simulate_move(actual_state.positions, move, actual_state.maze)
                new_state = State(actual_state.maze, new_positions, actual_state.moves + move)
                if frozenset(new_positions) not in self.visited:
                    self.queue.append(new_state)
                    self.visited.add(frozenset(new_positions))
        return None


if __name__ == '__main__':
    input_file = "zad_input.txt"
    output_file = "zad_output.txt"
    with open(input_file, 'r') as file:
        maze_str = file.read()
    m = Maze(maze_str)
    s = State(m, m.starts, "")
    s.reduce()
    b = BFS(s)
    answer = b.search().moves
    with open(output_file, 'w') as file:
        file.write(answer)