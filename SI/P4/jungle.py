import random
from copy import deepcopy
from statistics import mean
import sys

class Jungle:
    MAXIMAL_PASSIVE = float("inf")
    MX = 7
    MY = 9
    traps = {(2, 0), (4, 0), (3, 1), (2, 8), (4, 8), (3, 7)}
    ponds = {(x, y) for x in [1, 2, 4, 5] for y in [3, 4, 5]}
    dens = [(3, 8), (3, 0)]
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    rat, cat, dog, wolf, jaguar, tiger, lion, elephant = range(8)

    def __init__(self):
        self.board = self.initial_board()
        self.pieces = {0: {}, 1: {}}

        for y in range(Jungle.MY):
            for x in range(Jungle.MX):
                C = self.board[y][x]
                if C:
                    pl, pc = C
                    self.pieces[pl][pc] = (x, y)
        self.curplayer = 0
        self.peace_counter = 0
        self.winner = None

    def initial_board(self):
        pieces = """
        L.....T
        .D...C.
        R.J.W.E
        .......
        .......
        .......
        e.w.j.r
        .c...d.
        t.....l
        """

        B = [x.strip() for x in pieces.split() if len(x) > 0]
        T = dict(zip('rcdwjtle', range(8)))

        res = []
        for y in range(9):
            raw = 7 * [None]
            for x in range(7):
                c = B[y][x]
                if c != '.':
                    if 'A' <= c <= 'Z':
                        player = 1
                    else:
                        player = 0
                    raw[x] = (player, T[c.lower()])
            res.append(raw)
        return res

    def random_move(self, player):
        ms = self.moves(player)
        if ms:
            return random.choice(ms)
        return None

    def can_beat(self, p1, p2, pos1, pos2):
        if pos1 in Jungle.ponds and pos2 in Jungle.ponds:
            return True  # rat vs rat
        if pos1 in Jungle.ponds:
            return False  # rat in pond cannot beat any piece on land
        if p1 == Jungle.rat and p2 == Jungle.elephant:
            return True
        if p1 == Jungle.elephant and p2 == Jungle.rat:
            return False
        if p1 >= p2:
            return True
        if pos2 in Jungle.traps:
            return True
        return False

    def pieces_comparison(self):
        for i in range(7,-1,-1):
            ps = []
            for p in [0,1]:
                if i in self.pieces[p]:
                    ps.append(p)
            if len(ps) == 1:
                return ps[0]
        return None
                
    def rat_is_blocking(self, player_unused, pos, dx, dy):        
        x, y = pos
        nx = x + dx
        for player in [0,1]:
            if Jungle.rat not in self.pieces[1-player]:
                continue
            rx, ry = self.pieces[1-player][Jungle.rat]
            if (rx, ry) not in self.ponds:
                continue
            if dy != 0:
                if x == rx:
                    return True
            if dx != 0:
                if y == ry and abs(x-rx) <= 2 and abs(nx-rx) <= 2:
                    return True
        return False

    def draw(self):
        TT = {0: 'rcdwjtle', 1: 'RCDWJTLE'}
        for y in range(Jungle.MY):

            L = []
            for x in range(Jungle.MX):
                b = self.board[y][x]
                if b:
                    pl, pc = b
                    L.append(TT[pl][pc])
                else:
                    L.append('.')
            print(''.join(L))
        print('')

    def moves(self, player):
        res = []
        for p, pos in self.pieces[player].items():
            x, y = pos
            for (dx, dy) in Jungle.dirs:
                pos2 = (nx, ny) = (x+dx, y+dy)
                if 0 <= nx < Jungle.MX and 0 <= ny < Jungle.MY:
                    if Jungle.dens[player] == pos2:
                        continue
                    if pos2 in self.ponds:
                        if p not in (Jungle.rat, Jungle.tiger, Jungle.lion):
                            continue
                        if p == Jungle.tiger or p == Jungle.lion:
                            if dx != 0:
                                dx *= 3
                            if dy != 0:
                                dy *= 4
                            if self.rat_is_blocking(player, pos, dx, dy):
                                continue
                            pos2 = (nx, ny) = (x+dx, y+dy)
                    if self.board[ny][nx] is not None:
                        pl2, piece2 = self.board[ny][nx]
                        if pl2 == player:
                            continue
                        if not self.can_beat(p, piece2, pos, pos2):
                            continue
                    res.append((pos, pos2))
        return res

    def victory(self, player):
        oponent = 1-player        
        if len(self.pieces[oponent]) == 0:
            self.winner = player
            return True

        x, y = self.dens[oponent]
        if self.board[y][x]:
            self.winner = player
            return True
        
        # to make sure that the game is not stuck for random moves 
        if self.peace_counter >= Jungle.MAXIMAL_PASSIVE:           
            comp = self.pieces_comparison()
            if comp is None:
                self.winner = 1
            else:
                self.winner = comp
            return True
        
        return False
    
    def end(self):
        if not self.victory(0) and not self.victory(1):
            return False
        return True

    def do_move(self, m):
        self.curplayer = 1 - self.curplayer
        if m is None:
            return
        pos1, pos2 = m
        x, y = pos1
        pl, pc = self.board[y][x]

        x2, y2 = pos2
        if self.board[y2][x2]:  
            pl2, pc2 = self.board[y2][x2]
            del self.pieces[pl2][pc2]
            self.peace_counter = 0
        else:
            self.peace_counter += 1    

        self.pieces[pl][pc] = (x2, y2)
        self.board[y2][x2] = (pl, pc)
        self.board[y][x] = None

    def copy(self):
        jg_copy = Jungle()
        jg_copy.board = deepcopy(self.board)
        jg_copy.pieces = {0: self.pieces[0].copy(), 1: self.pieces[1].copy()}
        jg_copy.curplayer = self.curplayer
        jg_copy.peace_counter = self.peace_counter
        jg_copy.winner = self.winner
        return jg_copy

    def simulate_random_games(self, move, player, n=4):
        won = 0
        for _ in range(n):
            jg_copy = self.copy()
            jg_copy.do_move(move)
            while not jg_copy.end():
                next_move = jg_copy.random_move(jg_copy.curplayer)
                if next_move is None:
                    break
                jg_copy.do_move(next_move)
                
            if jg_copy.winner == player:
                won += 1
        return won

    def find_best_random(self, player):
        results = []
        for move in self.moves(player):
            score = self.simulate_random_games(move, player)
            results.append((score, move))
        results.sort(reverse=True, key=lambda x: x[0])
        results = [r for r in results if r[0] == results[0][0]]
        
        return random.choice(results)[1]

    def heuristic(self, player, weight=0.5):
        if self.end():
            if self.winner == player:
                return float("inf")
            elif self.winner == 1 - player:
                return float("-inf")

        gx0, gy0 = Jungle.dens[1]  
        gx1, gy1 = Jungle.dens[0]  

        dist0 = sum(abs(x - gx0) + abs(y - gy0) for (x, y) in self.pieces[0].values())
        dist1 = sum(abs(x - gx1) + abs(y - gy1) for (x, y) in self.pieces[1].values())

        p0 = sum(x for x in self.pieces[0].keys())
        p1 = sum(x for x in self.pieces[1].keys())

        if player == 0:
            return p0 - p1 + (dist1 - dist0) * weight
        else:
            return p1 - p0 + (dist0 - dist1) * weight

    def alphabeta_move(self, player, depth=5, alpha=float("-inf"), beta=float("inf")):
        my_player = 1 - (player==self.curplayer) #for heuristic to know as witch player algorithm is playing
        if depth == 0 or self.end():
            return self.heuristic(my_player), None
        
        best_move = None
        best_value = float('-inf') if 0 == player else float('inf')

        for move in self.moves(self.curplayer):
            new_board = self.copy()
            new_board.do_move(move)
            value, _ = new_board.alphabeta_move(1-player, depth - 1, alpha, beta)
            
            if 0 == player:
                if value > best_value:
                    best_value = value
                    best_move = move
                alpha = max(alpha, value)
            else:
                if value < best_value:
                    best_value = value
                    best_move = move
                beta = min(beta, value)

            if beta <= alpha:
                break

        return best_value, best_move
    
def play_games(n):
    results = {"ab": 0, "rand": 0}
    for _ in range(n):
        start_player = random.randint(0, 1)
        start_player = 0
        print(f"Starting player:", "ab" if start_player == 1 else "rand")
        jg = Jungle()
        while not jg.end():
            if not jg.curplayer == start_player:
                # print("ab...")
                move = jg.alphabeta_move(start_player, depth=4)[1]
            else:
                # print("random...")
                move = jg.find_best_random(jg.curplayer)
            jg.do_move(move)
            jg.draw()
        if jg.winner == 1:
            results["ab"] += 1
        else:
            results["rand"] += 1
        jg.draw()
    return results


class Player(object):
    def __init__(self):
        self.game = None
        self.my_player = None
        self.reset()

    def reset(self):
        self.my_player = 1
        self.game = Jungle()
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
                # print(args)
                move = tuple((int(m) for m in args[2:]))
                if move == (-1 ,-1 ,-1 ,-1 ):
                    move = None
                else:
                    move = ((move[0], move[1]), (move[2], move[3]))
                self.game.do_move(move)
            elif cmd == 'ONEMORE':
                self.reset()
                continue
            elif cmd == 'BYE':
                break
            else:
                assert cmd == 'UGO'
                self.my_player = 0

            move = self.game.alphabeta_move(0, 3)[1]

            if move is None:
                self.game.do_move(None)
                move = (-1, -1, -1, -1)
            else:
                self.game.do_move(move)
                move = (move[0][0], move[0][1], move[1][0], move[1][1])
            
            self.say('IDO %d %d %d %d' % move)


if __name__ == '__main__':
    # player = Player()
    # player.loop()
    res = play_games(10)
    print(res)