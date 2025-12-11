import javax.swing.*;
import java.awt.*;

public class CrossroadPanel extends JPanel{
    public final TrafficController controller = new TrafficController();
    private static int delay = 40; // milliseconds

    public CrossroadPanel() {
        new Timer(delay, e -> repaint()).start();
    }

    @Override
    public void paintComponent(Graphics g0) {
        super.paintComponent(g0);
        Graphics2D g = (Graphics2D) g0;

        g.setColor(Color.GRAY);
        g.fillRect(245, 0, 110, 600); // vertical
        g.fillRect(0, 245, 600, 110); // horizontal
        g.setColor(Color.WHITE);
        g.fillRect(295, 0, 10, 600); // vertical line
        g.fillRect(0, 295, 600, 10); // horizontal line
        g.setColor(Color.GRAY);
        g.fillRect(245, 245, 110, 110); // center

        for (Car c : controller.cars) {
            c.draw(g);
        }
    }
}
