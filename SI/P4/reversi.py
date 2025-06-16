import random
import sys
import time
import multiprocessing

M = 8
class Board:
    dirs  = [ (0,1), (1,0), (-1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1) ]
    
    def __init__(self, ab_move):
        self.board = self.initial_board()
        self.fields = set()
        self.move_list = []
        self.history = []
        self.ab_move = ab_move
        self.black_tokens = 2
        self.white_tokens = 2
        for i in range(M):
            for j in range(M):
                if self.board[i][j] == None:   
                    self.fields.add( (j,i) )
    
    def initial_board(self):
        B = [ [None] * M for i in range(M)]
        B[3][3] = 1
        B[4][4] = 1
        B[3][4] = 0
        B[4][3] = 0
        return B
                                                
    def draw(self):
        for i in range(M):
            res = []
            for j in range(M):
                b = self.board[i][j]
                if b == None:
                    res.append('.')
                elif b == 1:
                    res.append('#')
                else:
                    res.append('o')
            print (''.join(res)) 
        print            
                                   
    def moves(self, player):
        res = []
        for (x,y) in self.fields:
            if any( self.can_beat(x,y, direction, player) for direction in Board.dirs):
                res.append( (x,y) )
        if not res:
            return [None]
        return res               
    
    def can_beat(self, x,y, d, player):
        dx,dy = d
        x += dx
        y += dy
        cnt = 0
        while self.get(x,y) == 1-player:
            x += dx
            y += dy
            cnt += 1
        return cnt > 0 and self.get(x,y) == player
    
    def get(self, x,y):
        if 0 <= x < M and 0 <=y < M:
            return self.board[y][x]
        return None
                        
    def do_move(self, move, player):
        self.history.append([x[:] for x in self.board])
        self.move_list.append(move)
        
        if move == None:
            return
        x,y = move
        x0,y0 = move
        self.board[y][x] = player
        if player == 0:
            self.black_tokens += 1
        else:
            self.white_tokens += 1
        self.fields -= set([move])
        for dx,dy in self.dirs:
            x,y = x0,y0
            to_beat = []
            x += dx
            y += dy
            while self.get(x,y) == 1-player:
              to_beat.append( (x,y) )
              x += dx
              y += dy
            if self.get(x,y) == player:              
                for (nx,ny) in to_beat:
                    self.board[ny][nx] = player
                    if player == 0:
                        self.black_tokens += 1
                        self.white_tokens -= 1
                    else:
                        self.white_tokens += 1
                        self.black_tokens -= 1

                                                     
    def result(self):
        # res = 0
        # for y in range(M):
        #     for x in range(M):
        #         b = self.board[y][x]                
        #         if b == 0:
        #             res -= 1
        #         elif b == 1:
        #             res += 1
        res = self.black_tokens - self.white_tokens
        return res
                
    def end(self):
        if not self.fields:
            return True
        if len(self.move_list) < 2:
            return False
        return self.move_list[-1] == self.move_list[-2] == None 

    def random_move(self, player):
        ms = self.moves(player)
        if ms:
            return random.choice(ms)
        return [None]    
    
    def heuristic(self):
        res = 0
        opp = 1 - self.ab_move
        corner = 8

        res += -corner if self.board[0][0] == opp else corner if self.board[0][0] == self.ab_move else 0
        res += -corner if self.board[0][7] == opp else corner if self.board[0][7] == self.ab_move else 0
        res += -corner if self.board[7][0] == opp else corner if self.board[7][0] == self.ab_move else 0
        res += -corner if self.board[7][7] == opp else corner if self.board[7][7] == self.ab_move else 0

        empty_corner = 3
        if self.board[7][0]==None:
            res+=(empty_corner if self.board[6][1] == opp else -empty_corner if self.board[6][1] == self.ab_move else 0)
            res+=(empty_corner if self.board[7][1] == opp else -empty_corner if self.board[7][1] == self.ab_move else 0)
            res+=(empty_corner if self.board[6][0] == opp else -empty_corner if self.board[6][0] == self.ab_move else 0)
        if self.board[0][0]==None:
            res+=(empty_corner if self.board[1][1] == opp else -empty_corner if self.board[1][1] == self.ab_move else 0)
            res+=(empty_corner if self.board[0][1] == opp else -empty_corner if self.board[0][1] == self.ab_move else 0)
            res+=(empty_corner if self.board[1][0] == opp else -empty_corner if self.board[1][0] == self.ab_move else 0)
        if self.board[0][7]==None:
            res+=(empty_corner if self.board[1][6] == opp else -empty_corner if self.board[1][6] == self.ab_move else 0)
            res+=(empty_corner if self.board[0][6] == opp else -empty_corner if self.board[0][6] == self.ab_move else 0)
            res+=(empty_corner if self.board[1][7] == opp else -empty_corner if self.board[1][7] == self.ab_move else 0)
        if self.board[7][7]==None:
            res+=(empty_corner if self.board[6][6] == opp else -empty_corner if self.board[6][6] == self.ab_move else 0)
            res+=(empty_corner if self.board[7][6] == opp else -empty_corner if self.board[7][6] == self.ab_move else 0)
            res+=(empty_corner if self.board[6][7] == opp else -empty_corner if self.board[6][7] == self.ab_move else 0)

        for i in range(1, 7):
            res += -1 if self.board[0][i] == opp else 1 if self.board[0][i] == self.ab_move else 0
            res += -1 if self.board[i][0] == opp else 1 if self.board[i][0] == self.ab_move else 0
            res += -1 if self.board[7][i] == opp else 1 if self.board[7][i] == self.ab_move else 0
            res += -1 if self.board[i][7] == opp else 1 if self.board[i][7] == self.ab_move else 0
        
        return (len(self.move_list) + 5)/64*(self.black_tokens - self.white_tokens) + 1.0*res + 0.6*(len(self.moves(self.ab_move)) - len(self.moves(opp)))

    def alphabeta_move(self, player, depth=5, alpha=float("-inf"), beta=float("inf")):
        if self.end():
            return self.result()*1000, None
        if depth == 0:
            return self.heuristic(), None
        
        best_move = None
        best_value = float('-inf') if player == self.ab_move else float('inf')

        possible_moves = self.moves(player)

        for move in possible_moves:
            new_board = Board(self.ab_move)
            new_board.board = [row[:] for row in self.board]
            new_board.fields = set(self.fields)
            new_board.move_list = list(self.move_list)
            new_board.history = list(self.history)
            new_board.black_tokens = self.black_tokens
            new_board.white_tokens = self.white_tokens
            new_board.do_move(move, player)

            value, _ = new_board.alphabeta_move(1 - player, depth - 1, alpha, beta)

            if player == self.ab_move:
                if value > best_value:
                    best_value = value
                    best_move = move
                alpha = max(alpha, best_value)
            else:
                if value < best_value:
                    best_value = value
                    best_move = move
                beta = min(beta, best_value)
            if beta <= alpha:
                break

        return best_value, best_move


class Player(object):
    def __init__(self):
        self.game = None
        self.my_player = None
        self.reset()

    def reset(self):
        self.my_player = 1
        self.game = Board(self.my_player)
        self.say('RDY')

    def say(self, what):
        sys.stdout.write(what)
        sys.stdout.write('\n')
        sys.stdout.flush()

    def hear(self):
        line = sys.stdin.readline().strip()
        return line.split()[0], line.split()[1:]

    def loop(self):
        while True:
            cmd, args = self.hear()
            if cmd == 'HEDID':
                unused_move_timeout, unused_game_timeout = map(float, args[:2])
                move = tuple((int(m) for m in args[2:]))
                if move == (-1, -1):
                    move = None
                self.game.do_move(move, 1 - self.my_player)
            elif cmd == 'ONEMORE':
                self.reset()
                continue
            elif cmd == 'BYE':
                break
            else:
                assert cmd == 'UGO'
                assert not self.game.move_list
                self.my_player = 0
                self.game.ab_move = 0

            move = self.game.alphabeta_move(self.my_player, 4)[1]
            self.game.do_move(move, self.my_player)
            if move is None:
                move = (-1, -1)
            self.say('IDO %d %d' % move)

def play_games_mult(n, queue, d=4):
    results = {"AlphaBeta Agent Wins": 0, "Random Agent Wins": 0, "Draw": 0}
    for i in range(n):  # liczba gier do przeprowadzenia
        print(f"Game {i + 1}...")

        # 0 startuje ab, 1 startuje random
        start_agent = random.choice(["AB", "Rand"])
        if start_agent == "AB":
            B = Board(0)
        else:
            B = Board(1)
        curr_agent = start_agent
        player = 0
        while True:
            if curr_agent == "AB":
                _, move = B.alphabeta_move(player, depth=d, alpha=float('-inf'), beta=float('inf'))
            else:
                move = B.random_move(player)

            B.do_move(move, player)
            player = 1 - player
            curr_agent = "Rand" if curr_agent == "AB" else "AB"
            # B.draw()
            if B.end():
                # B.draw()
                break

        result = B.result()
        if result == 0:
            results["Draw"] += 1
        elif result > 0:
            if start_agent == "AB":
                results["AlphaBeta Agent Wins"] += 1
            else:
                results["Random Agent Wins"] += 1
        else:
            if start_agent == "AB":
                results["Random Agent Wins"] += 1
            else:
                results["AlphaBeta Agent Wins"] += 1

        # if (i+1)%50==0:
        #     print("Results so far:")
        #     for key, value in results.items():
        #         print(f"{key}: {value}")
    queue.put(results)
    return results

def play_multithread(k):
    time_start = time.time()
    num_processes = multiprocessing.cpu_count()
    results_queue = multiprocessing.Queue()
    processes = []
    n = (k // num_processes)

    for i in range(num_processes):
        process = multiprocessing.Process(target=play_games_mult, args=(n, results_queue, 2))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f"Time: {time.time() - time_start:.2f}s")
    final_results = {"AlphaBeta Agent Wins": 0, "Random Agent Wins": 0, "Draw": 0}
    while not results_queue.empty():
        results = results_queue.get()
        for key, value in results.items():
            final_results[key] += value

    print("Results:")
    for result, count in final_results.items():
        print(f"{result}: {count}")


if __name__ == '__main__':
    play_multithread(1000)
    # player = Player()
    # player.loop()

    # res = play_games(1000)
    # print("Final Results:")
    # for key, value in res.items():
    #     print(f"{key}: {value}")
    # TODO multithreading, time calculation, better heuristics