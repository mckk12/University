import java.awt.*;
import java.awt.event.*;
import java.io.*;
import javax.swing.*;

class SolitaireController {
    private SolitaireGame game;
    private SolitaireWindow window;
    private SolitaireGame.BoardType currentType = SolitaireGame.BoardType.BRITISH;
    private Color boardColor = Color.GREEN;
    private Color pieceColor = Color.RED;
    private boolean fillPieces = true;
    private boolean gameActive = false;
    private int gameStatus = 0; // 0 - active 1 - won 2 - lost
    private int selectedR = -1, selectedC = -1;


    public SolitaireController() {
        loadOrCreateGame();
        window = new SolitaireWindow(this);
        refresh();
    }

    private void loadOrCreateGame() {
        File f = new File("solitaire.ser");
        if (f.exists()) {
            try (ObjectInputStream o = new ObjectInputStream(new FileInputStream(f))) {
                game = (SolitaireGame) o.readObject();
                currentType = game.getBoardType();
                f.delete();
                gameActive = true;
                return;
            } catch (Exception ignored) {}
        }
        gameStatus = 0;
        gameActive = false;
        game = new SolitaireGame(SolitaireGame.BoardType.BRITISH);
    }

    public void startNewGame() {
        game.setBoard(currentType);
        selectedR = selectedC = -1;
        gameStatus = 0;
        gameActive = false;
        window.statusLabel.setText("Wykonaj pierwszy ruch.");
        refresh();
    }

    public void setBoardType(SolitaireGame.BoardType type) {
        currentType = type;
        startNewGame();
    }

    public void setBoardColor(Color color) {
        boardColor = color;
        refresh();
    }

    public void setPieceColor(Color color) {
        pieceColor = color;
        refresh();
    }

    public void setFillPieces(boolean fill) {
        fillPieces = fill;
        refresh();
    }

    public SolitaireGame.BoardType getBoardType() {
        return currentType;
    }

    public boolean isGameActive() {
        return gameActive;
    }

    private JPanel getPanel() { return window.boardPanel; }
    private void refresh() { window.repaint(); }

    public void draw(Graphics g) {
        int[][] b = game.getBoard();
        int size = game.getSize();
        int cell = (getPanel().getWidth()-100) / size;
        for (int r = 0; r < size; r++) {
            for (int c = 0; c < size; c++) {
                int x = c * cell;
                int y = r * cell;
                if (b[r][c] != -1) {
                    g.setColor(boardColor);
                    g.fillRect(x, y, cell, cell);
                    g.setColor(Color.BLACK);
                    g.drawRect(x, y, cell, cell);
                    if (b[r][c] == 1) {
                        g.setColor(pieceColor);
                        if (fillPieces) {
                            g.fillOval(x + 5, y + 5, cell - 10, cell - 10);
                        } else {
                            Stroke old = ((Graphics2D) g).getStroke();
                            ((Graphics2D) g).setStroke(new BasicStroke(3f));
                            g.drawOval(x + 5, y + 5, cell - 10, cell - 10);
                            ((Graphics2D) g).setStroke(old);
                        }
                    }
                } else {
                    g.setColor(getPanel().getBackground());
                    g.fillRect(x, y, cell, cell);
                }
                if (r == selectedR && c == selectedC) {
                    g.setColor(Color.BLACK);
                    Graphics2D g2 = (Graphics2D) g;
                    Stroke old = g2.getStroke();
                    g2.setStroke(new BasicStroke(4f));
                    g2.drawRect(x + 2, y + 2, cell - 4, cell - 4);
                    g2.setStroke(old);
                }
            }
        }
    }


    private void checkGameStatus() {
        int[][] b = game.getBoard();
        boolean canMove = false;
        for (int r = 0; r < game.getSize(); r++) {
            for (int c = 0; c < game.getSize(); c++) {
                if (b[r][c] == 1 && (
                    game.isValidPosition(r, c+2) && b[r][c+1] == 1 && b[r][c+2] == 0 ||
                    game.isValidPosition(r, c-2) && b[r][c-1] == 1 && b[r][c-2] == 0 ||
                    game.isValidPosition(r+2, c) && b[r+1][c] == 1 && b[r+2][c] == 0 ||
                    game.isValidPosition(r-2, c) && b[r-1][c] == 1 && b[r-2][c] == 0)) {
                        canMove = true;
                        break;
                }
            }
            if (canMove) break;
        }

        if (!canMove) {
            if (b[3][3] == 1) {
            gameActive = false;
            gameStatus = 1;
            window.statusLabel.setText("Gratulacje! Wygrałeś!");
        }else{
            int remaining = 0;
            for (int r = 0; r < game.getSize(); r++) {
                for (int c = 0; c < game.getSize(); c++) {
                    if (b[r][c] == 1) remaining++;
                }
            }
            gameActive = false;
            gameStatus = 2;
            window.statusLabel.setText("Koniec gry! Nie masz więcej ruchów. Pozostało pionów: " + remaining);
            }
        }
    }

    public MouseListener mouseHandler = new MouseAdapter() {
        @Override
        public void mouseClicked(MouseEvent e) {
            int cell = (getPanel().getWidth()-100) / game.getSize();
            int r = e.getY() / cell;
            int c = e.getX() / cell;
            handleClick(r, c);
        }
    };


    private void handleClick(int r, int c) {
        if (gameStatus>0) {
            window.statusLabel.setText("Gra zakończona. Rozpocznij nową grę.");
            return;
        }
        int[][] b = game.getBoard();
        if (selectedR == -1 && b[r][c] == 1) {
            selectedR = r;
            selectedC = c;
            window.statusLabel.setText("Wybrano pion.");
        }else if(selectedC == c && selectedR == r){
            selectedR = selectedC = -1;
            window.statusLabel.setText("Odznaczono pion.");
        }else if(selectedR != -1) {
            gameActive = true;
            if (game.move(selectedR, selectedC, r, c)) {
                window.statusLabel.setText("Wykonano ruch.");
                checkGameStatus();
            } else window.statusLabel.setText("Niepoprawny ruch.");
                selectedR = selectedC = -1;
        }
        refresh();
    }

    public void selectPiece() {
        if (gameStatus>0) {
            window.statusLabel.setText("Gra zakończona. Rozpocznij nową grę.");
            return;
        }
        window.statusLabel.setText("Wybierz pion używając strzałek");
        selectedC = selectedR = 3;
        refresh();
    }

    public void deselectPiece() {
        if (gameStatus>0) {
            window.statusLabel.setText("Gra zakończona. Rozpocznij nową grę.");
            return;
        }
        selectedR = selectedC = -1;
        window.statusLabel.setText("Odznaczono pion.");
        refresh();
    }

    public void moveUp() {
        if (gameStatus>0) return;
        gameActive = true;
        if (selectedR != -1 && selectedC != -1) {
            if (game.move(selectedR, selectedC, selectedR - 2, selectedC)) {
                window.statusLabel.setText("Wykonano ruch w górę.");
                checkGameStatus();
            } else {
                window.statusLabel.setText("Niepoprawny ruch w górę.");
            }
            selectedR = selectedC = -1;
            refresh();
        }
    }

    public void moveDown() {
        if (gameStatus>0) return;
        gameActive = true;
        if (selectedR != -1 && selectedC != -1) {
            if (game.move(selectedR, selectedC, selectedR + 2, selectedC)) {
                window.statusLabel.setText("Wykonano ruch w dół.");
                checkGameStatus();
            } else {
                window.statusLabel.setText("Niepoprawny ruch w dół.");
            }
            selectedR = selectedC = -1;
            refresh();
        }
    }

    public void moveLeft() {
        if (gameStatus>0) return;
        gameActive = true;
        if (selectedR != -1 && selectedC != -1) {
            if (game.move(selectedR, selectedC, selectedR, selectedC - 2)) {
                window.statusLabel.setText("Wykonano ruch w lewo.");
                checkGameStatus();
            } else {
                window.statusLabel.setText("Niepoprawny ruch w lewo.");
            }
            selectedR = selectedC = -1;
            refresh();
        }
    }

    public void moveRight() {
        if (gameStatus>0) return;
        gameActive = true;
        if (selectedR != -1 && selectedC != -1) {
            if (game.move(selectedR, selectedC, selectedR, selectedC + 2)) {
                window.statusLabel.setText("Wykonano ruch w prawo.");
                checkGameStatus();
            } else {
                window.statusLabel.setText("Niepoprawny ruch w prawo.");
            }
            selectedR = selectedC = -1;
            refresh();
        }
        
    }

    public KeyListener keyHandler = new KeyAdapter() {
        @Override
        public void keyPressed(KeyEvent e) {
            handleKeyboardInput(e);
            refresh();
        }
    };

    private void handleKeyboardInput(KeyEvent e) {
        if (gameStatus>0) {
            window.statusLabel.setText("Gra zakończona. Rozpocznij nową grę.");
            return;
        }
        int key = e.getKeyCode();
        if (e.isControlDown() || (e.getModifiersEx() & InputEvent.CTRL_DOWN_MASK) != 0) {
            return;
        }
        if (key == KeyEvent.VK_UP) {
            if (game.isValidPosition(selectedR - 1, selectedC)) {
                selectedR -= 1;
            }
        }
        else if (key == KeyEvent.VK_DOWN) {
            if (game.isValidPosition(selectedR + 1, selectedC)) {
                selectedR += 1;
            }
        }
        else if (key == KeyEvent.VK_LEFT) {
            if (game.isValidPosition(selectedR, selectedC - 1)) {
                selectedC -= 1;
            }
        }
        else if (key == KeyEvent.VK_RIGHT) {
            if (game.isValidPosition(selectedR, selectedC + 1)) {
                selectedC += 1;
            }
        }
    }

    private void saveAndExit() {
        try (ObjectOutputStream o = new ObjectOutputStream(new FileOutputStream("solitaire.ser"))) {
            o.writeObject(game);
        } catch (Exception ignored) {}
        System.exit(0);
    }

    public WindowListener windowHandler = new WindowAdapter() {
        @Override
        public void windowClosing(WindowEvent e) {
            saveAndExit();
        }
    };
    public void exit() { saveAndExit(); }

}
