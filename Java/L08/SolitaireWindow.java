import javax.swing.*;
import java.awt.*;
import java.awt.event.KeyEvent;

class SolitaireWindow extends JFrame {
    public BoardPanel boardPanel;
    public JLabel statusLabel;
    public JMenuBar menuBar;

    public SolitaireWindow(SolitaireController controller) {
        setTitle("Samotnik");
        setLayout(new BorderLayout());

        boardPanel = new BoardPanel(controller);
        statusLabel = new JLabel("Wybierz pion.");
        statusLabel.setFont(new Font("Arial", Font.BOLD, 18));

        gameMenu(controller);
        moveMenu(controller);
        settingsMenu(controller);
        helpMenu(controller);

        add(boardPanel, BorderLayout.CENTER);
        add(statusLabel, BorderLayout.SOUTH);

        setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
        addWindowListener(controller.windowHandler);

        setSize(800, 800);
        setLocationRelativeTo(null);
        setVisible(true);
        addKeyListener(controller.keyHandler);
    }

    private void gameMenu(SolitaireController controller) {
        menuBar = new JMenuBar();

        JMenu gameMenu = new JMenu("Gra");
        gameMenu.setMnemonic(KeyEvent.VK_G);
        JMenuItem newGame = new JMenuItem("Nowa gra");
        newGame.addActionListener(e -> controller.startNewGame());
        newGame.setMnemonic(KeyEvent.VK_N);
        JMenuItem exit = new JMenuItem("Koniec");
        exit.addActionListener(e -> controller.exit());
        exit.setMnemonic(KeyEvent.VK_K);

        gameMenu.add(newGame);
        gameMenu.add(exit);
        menuBar.add(gameMenu);
        setJMenuBar(menuBar);
    }

    private void moveMenu(SolitaireController controller) {
        JMenu moveMenu = new JMenu("Ruchy");
        JMenuItem select = new JMenuItem("Wybierz pion");
        select.addActionListener(e -> controller.selectPiece());
        select.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_S, 0));
        JMenuItem deselect = new JMenuItem("Odznacz pion");
        deselect.addActionListener(e -> controller.deselectPiece());
        deselect.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_D, 0));
        JMenuItem up = new JMenuItem("Ruch w górę");
        up.addActionListener(e -> controller.moveUp());
        up.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_UP, java.awt.event.InputEvent.CTRL_DOWN_MASK));
        JMenuItem down = new JMenuItem("Ruch w dół");
        down.addActionListener(e -> controller.moveDown());
        down.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_DOWN, java.awt.event.InputEvent.CTRL_DOWN_MASK));
        JMenuItem left = new JMenuItem("Ruch w lewo");
        left.addActionListener(e -> controller.moveLeft());
        left.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_LEFT, java.awt.event.InputEvent.CTRL_DOWN_MASK));
        JMenuItem right = new JMenuItem("Ruch w prawo");
        right.addActionListener(e -> controller.moveRight());
        right.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_RIGHT, java.awt.event.InputEvent.CTRL_DOWN_MASK));
        moveMenu.add(select);
        moveMenu.add(deselect);
        moveMenu.add(up);
        moveMenu.add(down);
        moveMenu.add(left);
        moveMenu.add(right);
        menuBar.add(moveMenu);
    }

    private void settingsMenu(SolitaireController controller) {
        JMenu settingsMenu = new JMenu("Ustawienia");
        JRadioButtonMenuItem british = new JRadioButtonMenuItem("Brytyjska");
        JRadioButtonMenuItem european = new JRadioButtonMenuItem("Europejska"); 
        british.addActionListener(e -> controller.setBoardType(SolitaireGame.BoardType.BRITISH));
        european.addActionListener(e -> controller.setBoardType(SolitaireGame.BoardType.EUROPEAN));
        ButtonGroup boardGroup = new ButtonGroup();
        boardGroup.add(british);
        boardGroup.add(european);

        SolitaireGame.BoardType current = controller.getBoardType();
        if (current == SolitaireGame.BoardType.BRITISH) {
        british.setSelected(true);
        } else if (current == SolitaireGame.BoardType.EUROPEAN) {
        european.setSelected(true);
        }

        JMenuItem boardColorItem = new JMenuItem("Wybierz kolor planszy");
        boardColorItem.addActionListener(e -> {
            Color chosen = JColorChooser.showDialog(this, "Wybierz kolor planszy", Color.GREEN);
            if (chosen != null) controller.setBoardColor(chosen);
        });

        JMenuItem pieceColorItem = new JMenuItem("Wybierz kolor pionów");
        pieceColorItem.addActionListener(e -> {
            Color chosen = JColorChooser.showDialog(this, "Wybierz kolor pionów", Color.RED);
            if (chosen != null) controller.setPieceColor(chosen);
        });

        JCheckBoxMenuItem fillPieces = new JCheckBoxMenuItem("Wypełniaj wnętrze pionów");
        fillPieces.setSelected(true);
        fillPieces.addItemListener(e -> controller.setFillPieces(fillPieces.isSelected()));
        

        settingsMenu.add(british);
        settingsMenu.add(european);
        settingsMenu.addSeparator();
        settingsMenu.add(boardColorItem);
        settingsMenu.add(pieceColorItem);
        settingsMenu.addSeparator();
        settingsMenu.add(fillPieces);

        settingsMenu.addMenuListener(new javax.swing.event.MenuListener() {
            public void menuSelected(javax.swing.event.MenuEvent e) {
                boolean active = controller.isGameActive();
                british.setEnabled(!active);
                european.setEnabled(!active);
            }
            public void menuDeselected(javax.swing.event.MenuEvent e) {}
            public void menuCanceled(javax.swing.event.MenuEvent e) {}
        });

        menuBar.add(settingsMenu);
    }

    private void helpMenu(SolitaireController controller) {
        JMenu helpMenu = new JMenu("Pomoc");
        JMenuItem aboutGame = new JMenuItem("O grze");
        aboutGame.addActionListener(e -> showAbout());
        JMenuItem aboutApp = new JMenuItem("O aplikacji");
        aboutApp.addActionListener(e -> showAboutApp());

        helpMenu.add(aboutGame);
        helpMenu.add(aboutApp);

        menuBar.add(Box.createHorizontalGlue());
        menuBar.add(helpMenu);
    }

    private void showAbout() {
        JOptionPane.showMessageDialog(this,
                "Samotnik to gra planszowa, w której celem jest usunięcie wszystkich pionów z planszy oprócz jednego.\n" +
                "Piony poruszają się skacząc nad innymi pionami na puste pola.\n" +
                "Dostępne są dwie wersje planszy: brytyjska i europejska.",
                "O grze Samotnik",
                JOptionPane.INFORMATION_MESSAGE);
    }

    private void showAboutApp() {
        JOptionPane.showMessageDialog(this,
                "Aplikacja Samotnik została stworzona jako projekt edukacyjny.\n" +
                "Autor: Maciej Ciepiela\n" +
                "Wersja: 1.0\n" +
                "Data powstania: 9.12.2025",
                "O aplikacji Samotnik",
                JOptionPane.INFORMATION_MESSAGE);
    }
}

class BoardPanel extends JPanel {
    private SolitaireController controller;

    public BoardPanel(SolitaireController controller) {
        this.controller = controller;
        addMouseListener(controller.mouseHandler);
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        controller.draw(g);
    }

}
