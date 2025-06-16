import chess
import random
# import chess.syzygy
import chess.svg
import webbrowser
import sys

DEPTH = 3

class Chess:
    dirs = [-9, -8, -7, 1, 9, 8, 7, -1]

    def __init__(self):
        self.board = chess.Board()
        # self.endgameTable = chess.syzygy.open_tablebase("data/syzygy/regular")
    
    def draw(self):
        print (self.board)  
        print ()  

    def moves(self, player):
        return self.board.legal_moves

    def end(self):
        return self.board.is_game_over()

    def calculate_material(self, player):
        return  (len(self.board.pieces(chess.QUEEN, player)) * 9 \
                + len(self.board.pieces(chess.ROOK, player)) * 5 \
                + len(self.board.pieces(chess.BISHOP, player)) * 3 \
                + len(self.board.pieces(chess.KNIGHT, player)) * 3 \
                + len(self.board.pieces(chess.PAWN, player))) 
     
    # przewaga materialu
    def material_advantage(self, player):
        return self.calculate_material(player) - self.calculate_material(not player)

    # ruchowosc
    def mobility_advantage(self, player):
        temp_board = self.board.copy()
        temp_board.turn = player
        my_pl = len(list(temp_board.legal_moves))
        temp_board.turn = not player
        opp_pl = len(list(temp_board.legal_moves))
        return my_pl - opp_pl 
    
    # uklad pionow
    def pawn_structure(self, player):
        pawn_positions = self.board.pieces(chess.PAWN, player)
        if not pawn_positions:
            return 0
        dist_to_closest_pawn = []
        backward_pawns = 0
        doubled_pawns = 0
        for pos in pawn_positions:
            if player == chess.WHITE:
                if self.board.piece_type_at(pos + 8) == chess.PAWN:
                    doubled_pawns += 1
                if pos % 8 == 0:
                    if self.board.piece_type_at(pos - 7) != chess.PAWN:
                        backward_pawns += 1
                elif pos % 8 == 7:
                    if self.board.piece_type_at(pos - 9) != chess.PAWN:
                        backward_pawns += 1
                else:
                    if self.board.piece_type_at(pos - 7) != chess.PAWN and self.board.piece_type_at(pos - 9) != chess.PAWN:
                        backward_pawns += 1
            else:  
                if self.board.piece_type_at(pos - 8) == chess.PAWN:
                    doubled_pawns += 1
                if pos % 8 == 0:
                    if self.board.piece_type_at(pos + 9) != chess.PAWN:
                        backward_pawns += 1
                elif pos % 8 == 7:
                    if self.board.piece_type_at(pos + 7) != chess.PAWN:
                        backward_pawns += 1
                else:
                    if self.board.piece_type_at(pos + 7) != chess.PAWN and self.board.piece_type_at(pos + 9) != chess.PAWN:
                        backward_pawns += 1
            closest_pawn = min(pawn_positions, key=lambda p: chess.square_manhattan_distance(p, pos))
            dist_to_closest_pawn.append(chess.square_manhattan_distance(pos, closest_pawn))
        isolation = sum(dist_to_closest_pawn) / len(dist_to_closest_pawn) if dist_to_closest_pawn else 0
        return -(isolation+backward_pawns+doubled_pawns)  

    # bezpieczenstwo krola
    def king_safety(self, player):
        temp_board = self.board.copy()
        temp_board.turn = not player
        opp_moves = set(m.to_square for m in temp_board.legal_moves)
        king_pos = self.board.king(player)
        around = [king_pos + d for d in self.dirs]
        squares = 0
        pieces_around = 0
        for pos in around:
            if pos < 0 or pos > 63 or (king_pos%8==0 and pos%8==7) or (king_pos%8==7 and pos%8==0):
                continue
            squares += 1
            if self.board.piece_at(pos) or pos not in opp_moves:
                pieces_around+=1
        return pieces_around/squares

    # pola pod kontrola
    def fields_control(self, player):
        temp_board = self.board.copy()
        temp_board.turn = player
        possible_moves = temp_board.legal_moves
        possible_to = set([m.to_square for m in possible_moves])
        return len(possible_to)

    # bierki pod grozba bicia
    def under_attack(self, player):
        temp_board = self.board.copy()
        temp_board.turn = not player
        count = 0
        for move in temp_board.legal_moves:
            if self.board.piece_at(move.to_square):
                count+=1
        return -count
    
    # wagi wymagają lepszego dopasowania, bazującego na eksperymentach, póki co spęłniaja swoje zadanie
    def heuristic(self, player):
        return  1.6*self.material_advantage(player) + 0.3 * self.mobility_advantage(player) + \
                1*self.pawn_structure(player) + self.king_safety(player) + \
                0.7 * self.fields_control(player) + 0.1*self.under_attack(player) + len(self.board.checkers())*2
    
    def alphabeta_move(self, player, depth=5, alpha=float("-inf"), beta=float("inf")):
        # if len(self.board.piece_map) <= 7:
        #     return 10000 * self.endgameTable.probe_wdl(self.board), None
        if self.board.is_game_over():
            out = self.board.outcome()
            if out.winner is None:
                return 0, None
            return 10000 if out.winner == player else -10000, None
        if depth == 0:
            return self.heuristic(player), None
        
        best_move = None
        best_value = float('-inf') if player == self.board.turn else float('inf')

        possible_moves = self.moves(self.board.turn)

        for move in possible_moves:
            temp_chess = Chess()
            temp_chess.board = self.board.copy()
            # temp_chess.endgameTable = self.endgameTable
            temp_chess.board.push(move)

            value, _ = temp_chess.alphabeta_move(player, depth - 1, alpha, beta)

            if player == self.board.turn:
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
    
    def visualize(self):
        svg_board = chess.svg.board(self.board, size=700, coordinates=True)
        with open("chess_board.html", "w") as html_file:
            html_file.write('<html><body>\n')
            html_file.write(svg_board)
            html_file.write('\n</body></html>')
        webbrowser.open("chess_board.html")
    
def game_vs_random():
    game = Chess()
    random_playing = random.choice([chess.WHITE, chess.BLACK])
    ab_playing = not random_playing
    while not game.board.is_game_over():
        if game.board.turn == random_playing:
            move = random.choice(list(game.board.legal_moves))
        else:
            _, move = game.alphabeta_move(ab_playing, 3)
        if move is None:
            print("No legal moves available, game over.")
            break
        game.board.push(move)
        game.visualize()
        # print(game.board)
        # print()
    print("Game over")
    print("Winner:", "Alpha-Beta" if game.board.outcome().winner == ab_playing else "Random" if game.board.outcome().winner == random_playing else "Draw")


class Player(object):
    def __init__(self):
        self.game = None
        self.my_player = None
        self.reset()

    def reset(self):
        self.my_player = chess.BLACK
        self.game = Chess()
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
                move = chess.Move.from_uci(args[2])

                self.game.board.push(move)
            elif cmd == 'ONEMORE':
                self.reset()
                continue
            elif cmd == 'BYE':
                break
            else:
                assert cmd == 'UGO'
                self.my_player = chess.WHITE

 
            move = self.game.alphabeta_move(self.my_player, DEPTH)[1]

            self.game.board.push(move)
            
            self.say('IDO '+ str(move))

if __name__ == "__main__":
    game_vs_random()
    # player = Player()
    # player.loop()