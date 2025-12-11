import javax.swing.*;
import java.awt.*;

public class CrossroadApp extends JFrame {

    private final CrossroadPanel panel = new CrossroadPanel();
    private final TrafficController controller = panel.controller;
    private final int MAX_CARS = 20;

    // Cooldown (ms) per road to prevent rapid spawns
    private static final long COOLDOWN_MS = 1000;
    private final long[] lastSpawnTime = new long[]{0,0,0,0}; // north,east,south,west

    public CrossroadApp() {
        setTitle("Crossroad Simulation");
        setSize(600, 600);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new BorderLayout());
        add(panel, BorderLayout.CENTER);
        panel.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                handleMouseClick(evt.getX(), evt.getY());
            }
        });
    }

    private void handleMouseClick(int x, int y) {
        int roadId = -1;
        if (x >= 250 && x <= 350) {
            if (y < 250) roadId = 0; // north
            else if (y > 350) roadId = 2; // south
        } else if (y >= 250 && y <= 350) {
            if (x < 250) roadId = 3; // west
            else if (x > 350) roadId = 1; // east
        }

        if (roadId != -1) {
            addCarOnclick(roadId);
        }
    }

    private void addCarOnclick(int roadId) {
        long now = System.currentTimeMillis();
        if (now - lastSpawnTime[roadId] < COOLDOWN_MS) return;

        if (controller.cars.size() >= MAX_CARS) return;
        lastSpawnTime[roadId] = now;

        Car c = new Car(roadId, controller);
        controller.cars.add(c);
        c.start();
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new CrossroadApp().setVisible(true));
    }
}
