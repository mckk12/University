import javax.swing.SwingUtilities;

public class SolitaireApp {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new SolitaireController());
    }
}