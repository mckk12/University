'''
Firstly we create a Postion class, which will represent the current state of the game. It will have the following attributes:
- earlier_position: the previous state of the game
- to_move: the color of the player to move
- w_king: the position of the white king
- w_rook: the position of the white rook
- b_king: the position of the black king
And for every postion we will have methods generating all posible move in the given state.
Next we create a BFS class, which will be responsible for searching for the checkmate. It will have the following attributes:
- root: the starting position
- queue: the queue of states to check
- visited: the set of visited states
Then we begin searching for the checkmate. We start with the given example state and check all possible moves from it. 
If we find the checkmate we return the state, otherwise we add all possible moves to the queue and continue the search.
Then for Position class we have some printing methods to ease the debugging and to save the states to the file.
In calculations, the board we see as a XY plane, where A1 is (1,1) and H8 is (8,8). 
We use simple ord and chr to quickly convert between letters and numbers.
'''

def read_file(file):
    situations = []
    with open(file, "r") as f:
        for line in f:
            situations.append(line.strip().split())
    return situations

class Position:
    def __init__(self, earlier, info, mc = 0):
        self.earlier_position = earlier
        self.to_move = info[0]
        self.w_king = info[1]
        self.w_rook = info[2]
        self.b_king = info[3]
        self.move_count = mc
    
    def w_king_moves(self):
        moves = []
        all_moves = [(self.w_king[0]+1, self.w_king[1]), (self.w_king[0]-1, self.w_king[1]), (self.w_king[0], self.w_king[1]+1), (self.w_king[0], self.w_king[1]-1),
                          (self.w_king[0]+1, self.w_king[1]+1), (self.w_king[0]-1, self.w_king[1]-1), (self.w_king[0]+1, self.w_king[1]-1), (self.w_king[0]-1, self.w_king[1]+1)]  
        for move in all_moves:
            # move is on the board, not in the same position as rook, is not puting the king in check
            if 1 <= move[0] <= 8 and 1 <= move[1] <= 8 and move != self.w_rook and not (abs(move[0]-self.b_king[0]) <= 1 and abs(move[1]-self.b_king[1]) <= 1):
                moves.append(move)
        return moves

    def w_rook_moves(self):
        moves = []
        all_moves = [(self.w_rook[0], i) for i in range(1, 9) if i!=self.w_rook[1]] + [(i, self.w_rook[1]) for i in range(1, 9) if i!=self.w_rook[0]]
        # print(all_moves)
        for move in all_moves:
            # move is not putting rook in range of bking and rook is not phasing through wking
            if not (abs(move[0]-self.b_king[0]) <= 1 and abs(move[1]-self.b_king[1]) <= 1) and not \
            (self.w_rook[0] == self.w_king[0] and ((self.w_rook[1]<self.w_king[1] and move[1]>=self.w_king[1]) or (self.w_rook[1]>self.w_king[1] and move[1]<=self.w_king[1])) or
            self.w_rook[1] == self.w_king[1] and ((self.w_rook[0]<self.w_king[0] and move[0]>=self.w_king[0]) or (self.w_rook[0]>self.w_king[0] and move[0]<=self.w_king[0]))):
                moves.append(move)
        return(moves)
    
    def b_king_moves(self):
        moves = []
        all_moves = [(self.b_king[0]+1, self.b_king[1]), (self.b_king[0]-1, self.b_king[1]), (self.b_king[0], self.b_king[1]+1), (self.b_king[0], self.b_king[1]-1),
                          (self.b_king[0]+1, self.b_king[1]+1), (self.b_king[0]-1, self.b_king[1]-1), (self.b_king[0]+1, self.b_king[1]-1), (self.b_king[0]-1, self.b_king[1]+1)]  
        for move in all_moves:
            # move is on the board and king is not putting itself in check of wking nor wrook
            if 1 <= move[0] <= 8 and 1 <= move[1] <= 8 and not (abs(move[0]-self.w_king[0]) <= 1 and abs(move[1]-self.w_king[1]) <= 1) and not (self.w_rook[0] == move[0] or self.w_rook[1] == move[1]):
                moves.append(move)
        return moves
    
    def is_checkmate(self):
        if self.b_king_moves() == [] and (self.w_rook[0] == self.b_king[0] or self.w_rook[1] == self.b_king[1]):
            return True

    def print_board(self):
        board = [["_"]*8]*8

        board[-self.w_king[1]] = board[-self.w_king[1]][:self.w_king[0]-1] + ["K"] + board[-self.w_king[1]][self.w_king[0]:]
        board[-self.w_rook[1]] = board[-self.w_rook[1]][:self.w_rook[0]-1] + ["R"] + board[-self.w_rook[1]][self.w_rook[0]:]
        board[-self.b_king[1]] = board[-self.b_king[1]][:self.b_king[0]-1] + ["k"] + board[-self.b_king[1]][self.b_king[0]:]

        print("  A B C D E F G H")
        for i, row in enumerate(board):
            print(i+1, " ".join(row), i+1)
        print("  A B C D E F G H")
        print("\n")
    
    def print_sequence(self):
        sequence = []
        current = self
        while current:
            sequence.append(current)
            current = current.earlier_position
        sequence.reverse()
        for pos in sequence:
            pos.print_board()
        
    
    def positions_to_file(self, file, number):
        f = open(file, "a")
        f.write(f"Situation {number}:\n")
        sequence = []
        current = self
        while current:
            sequence.append(current)
            current = current.earlier_position
        sequence.reverse()
        for pos in sequence:
            w_k = chr(pos.w_king[0]+96) + str(pos.w_king[1])
            w_r = chr(pos.w_rook[0]+96) + str(pos.w_rook[1])
            b_k = chr(pos.b_king[0]+96) + str(pos.b_king[1])
            f.write(f"{pos.to_move} {w_k} {w_r} {b_k}\n")
        f.write("\n")
        f.close()
    

class BFS:
    def __init__(self, root):
        self.root = root
        self.queue = [root]
        self.visited = set()

    def search(self):
        while self.queue:
            current = self.queue.pop(0)
            if current.is_checkmate():
                return current
            else:
                if current.to_move == "white":
                    for move in current.w_king_moves():
                        new_position = ("black", move, current.w_rook, current.b_king)
                        if new_position not in self.visited:
                            self.queue.append(Position(current, new_position, current.move_count+1))
                            self.visited.add(new_position)
                    for move in current.w_rook_moves():
                        new_position = ("black", current.w_king, move, current.b_king)
                        if new_position not in self.visited:
                            self.queue.append(Position(current, new_position, current.move_count+1))
                            self.visited.add(new_position)
                else:
                    for move in current.b_king_moves():
                        new_position = ("white", current.w_king, current.w_rook, move)
                        if new_position not in self.visited:
                            self.queue.append(Position(current, new_position, current.move_count+1))
                            self.visited.add(new_position)
        return None

if __name__ == "__main__":
    example_file = "zad1_input.txt"
    file_to_save = "zad1_output.txt"
    
    f = open(file_to_save, "w")
    situations = read_file(example_file)
    # situations = [("white", "c2", "a8", "a1")]
    for i, sit in enumerate(situations):
        # -96 for letters
        w_king = (ord(sit[1][0])-96,int(sit[1][1]))
        w_rook = (ord(sit[2][0])-96,int(sit[2][1]))
        b_king = (ord(sit[3][0])-96,int(sit[3][1]))
        # print(w_king, w_rook, b_king)

        root = Position(None, (sit[0], w_king, w_rook, b_king))
        # root.print_board()
        bfs = BFS(root)
        result = bfs.search()
        if result:
            print(f"Result for the {i+1}-th situation (mate in {result.move_count} moves):")
            # result.positions_to_file(file_to_save, i+1)
            f.write(str(result.move_count))
            result.print_sequence()
        else:
            print("INF")

    f.close()
