import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

public class Powierzchnia extends Canvas {
    private ArrayList<Kreska> kreski;
    private Point start = null;
    private Point current = null;
    private Color currentColor = Color.BLACK;

    public Powierzchnia() {
        kreski = new ArrayList<>();
        addMouseListener(new MouseAdapter() {
            public void mousePressed(MouseEvent evt) {
                start = evt.getPoint();
            }

            public void mouseReleased(MouseEvent evt) {
                Point end = evt.getPoint();
                if (contains(end)) {
                    kreski.add(new Kreska(start, end, currentColor));
                }
                start = null;
                current = null;
                repaint();
            }
        });

        addMouseMotionListener(new MouseMotionAdapter() {
            public void mouseDragged(MouseEvent evt) {
                current = evt.getPoint();
                repaint();
            }
        });

        addKeyListener(new KeyAdapter() {
            public void keyPressed(KeyEvent ke){
                System.out.println("Key pressed: " + ke.getKeyCode());
                switch (ke.getKeyCode()) {
                    case KeyEvent.VK_BACK_SPACE:
                        clearAll();
                        break;
                    case KeyEvent.VK_F:
                        removeFirst();
                        break;
                    case KeyEvent.VK_L:
                    case KeyEvent.VK_B:
                        removeLast();
                        break;
                }
            }
        });
    }

    public void paint(Graphics gr) {
        for (Kreska k : kreski) {
            gr.setColor(k.kolor);
            gr.drawLine(k.poczatek.x, k.poczatek.y, k.koniec.x, k.koniec.y);
        }
        if (start != null && current != null) {
            gr.setColor(Color.GRAY);
            gr.drawLine(start.x, start.y, current.x, current.y);
        }
    }

    public void clearAll() {
        kreski.clear();
        repaint();
    }

    public void removeFirst() {
        if (!kreski.isEmpty()) {
            kreski.remove(0);
            repaint();
        }
    }

    public void removeLast() {
        if (!kreski.isEmpty()) {
            kreski.remove(kreski.size() - 1);
            repaint();
        }
    }

    public void setCurrentColor(Color color) {
        this.currentColor = color;
    }

    
}
