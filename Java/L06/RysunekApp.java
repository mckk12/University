import java.awt.*;
import java.awt.event.*;

public class RysunekApp extends Frame{
    private Powierzchnia powierzchnia;
    private CheckboxGroup kolory;

    public RysunekApp(){
        super("Rysunek - Kreski");
        setSize(800, 600);
        setLayout(new BorderLayout());

        powierzchnia = new Powierzchnia();
        add(powierzchnia, BorderLayout.CENTER);

        Panel panel = new Panel();
        panel.setLayout(new GridLayout(0, 1));
        kolory = new CheckboxGroup();
        String[] nazwyKolorow = {"Czarny", "Czerwony", "Zielony", "Niebieski", "Zolty"};
        Color[] koloryTab = {Color.BLACK, Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW};

        for (int i = 0; i < nazwyKolorow.length; i++) {
            Checkbox cb = new Checkbox(nazwyKolorow[i], kolory, i == 0);
            Color kolor = koloryTab[i];
            cb.addItemListener(new ItemListener() {
                public void itemStateChanged(ItemEvent e) {
                    powierzchnia.setCurrentColor(kolor);
                }
            });
            panel.add(cb);
        }
        add(panel, BorderLayout.EAST);

        addWindowListener(new WindowAdapter(){
            public void windowClosing(WindowEvent we){
                dispose();
            }
            public void windowActivated(WindowEvent we){
                powierzchnia.requestFocus();
            }
        });

        setVisible(true);
    }

    public static void main(String[] args){
        new RysunekApp();
    }
}
