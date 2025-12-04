import java.io.Serializable;

class SolitaireGame implements Serializable {
    public enum BoardType {BRITISH, EUROPEAN};
    private int[][] board;
    private BoardType boardType;

    public SolitaireGame(BoardType type) {
        setBoard(type);
    }

    public void setBoard(BoardType type){
        this.boardType = type;
        this.board = new int[7][7];
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                if (!isValidPosition(i, j)) board[i][j] = -1;
                else board[i][j] = 1;
                }
            }
            board[3][3] = 0;
    }

    public boolean isValidPosition(int r, int c) {
        if (boardType == BoardType.BRITISH) {
            return !((r < 2 || r > 4) && (c < 2 || c > 4)) && !(r<0 || r>6 || c<0 || c>6);
        } else {
            return !(((r == 0 || r == 6) && (c < 2 || c > 4)) || ((r == 1 || r == 5) && (c < 1 || c > 5)));
        }
    }

    public boolean move(int fromR, int fromC, int toR, int toC) {
        if (isValidPosition(toR, toC) && isValidPosition(fromR, fromC)) {
            int dr = toR - fromR;
            int dc = toC - fromC;
            if (Math.abs(dr) == 2 && dc == 0 || Math.abs(dc) == 2 && dr == 0) {
                int rm = fromR + dr/2;
                int cm = fromC + dc/2;
                if (board[fromR][fromC] == 1 && board[rm][cm] == 1 && board[toR][toC] == 0) {
                    board[fromR][fromC] = 0;
                    board[rm][cm] = 0;
                    board[toR][toC] = 1;
                    return true;
                }
            }
        }
        return false;   
    }

    public int[][] getBoard() {
        return board;
    }

    public int getSize() {
        return board.length;
    }

    public BoardType getBoardType() {
        return boardType;
    }
}