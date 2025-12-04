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
        gameActive = false;
        game = new SolitaireGame(SolitaireGame.BoardType.BRITISH);
    }

    public void startNewGame() {
        game.setBoard(currentType);
        selectedR = selectedC = -1;
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

    public void moveUp() {
        gameActive = true;
        if (selectedR != -1 && selectedC != -1) {
            if (game.move(selectedR, selectedC, selectedR - 2, selectedC)) {
                window.statusLabel.setText("Wykonano ruch w górę.");
            } else {
                window.statusLabel.setText("Niepoprawny ruch w górę.");
            }
            selectedR = selectedC = -1;
            refresh();
        }
    }

    public void moveDown() {
        gameActive = true;
        if (selectedR != -1 && selectedC != -1) {
            if (game.move(selectedR, selectedC, selectedR + 2, selectedC)) {
                window.statusLabel.setText("Wykonano ruch w dół.");
            } else {
                window.statusLabel.setText("Niepoprawny ruch w dół.");
            }
            selectedR = selectedC = -1;
            refresh();
        }
    }

    public void moveLeft() {
        gameActive = true;
        if (selectedR != -1 && selectedC != -1) {
            if (game.move(selectedR, selectedC, selectedR, selectedC - 2)) {
                window.statusLabel.setText("Wykonano ruch w lewo.");
            } else {
                window.statusLabel.setText("Niepoprawny ruch w lewo.");
            }
            selectedR = selectedC = -1;
            refresh();
        }
    }

    public void moveRight() {
        gameActive = true;
        if (selectedR != -1 && selectedC != -1) {
            if (game.move(selectedR, selectedC, selectedR, selectedC + 2)) {
                window.statusLabel.setText("Wykonano ruch w prawo.");
            } else {
                window.statusLabel.setText("Niepoprawny ruch w prawo.");
            }
            selectedR = selectedC = -1;
            refresh();
        }
    }

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
                            g.drawOval(x + 5, y + 5, cell - 10, cell - 10);
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
                    g2.setStroke(new BasicStroke(4f)); // set thickness here
                    g2.drawRect(x + 2, y + 2, cell - 4, cell - 4);
                    g2.setStroke(old);
                }
            }
        }
    }


    private JPanel getPanel() { return window.boardPanel; }
    private void refresh() { window.repaint(); }


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
            } else window.statusLabel.setText("Niepoprawny ruch.");
                selectedR = selectedC = -1;
        }
        refresh();
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
