import java.awt.*;
import java.util.Random;

public class Car extends Thread{
    private int speed;
    public int currentRoadIndex; // 0 - north, 1 - east, 2 - south, 3 - west
    public int turnDirection; // -1 - right, 0 - straight, 1 - left
    private int x, y;
    private TrafficController controller;
    private int newSpeed = -1;

    public Car(int currentRoadIndex, TrafficController controller) {
        this.speed = new Random().nextInt(3) + 2;
        this.currentRoadIndex = currentRoadIndex;
        this.turnDirection = new Random().nextInt(3) - 1;
        this.controller = controller;

        switch (currentRoadIndex) {
            case 0 -> { x = 260; y = -40; } // north
            case 2 -> { x = 320; y = 640; } // south
            case 1  -> { x = 640; y = 260; } // east
            case 3  -> { x = -40; y = 320; } // west
        }
    }

    public int getX() {
        return x;
    }
    public int getY() {
        return y;
    }

    public int getCurrentSpeed() {
        if (newSpeed > -1) {
            return newSpeed;
        }
        return speed;
    }

    public int getOldSpeed() {
        return speed;
    }

    public void changeSpeed(int s) {
        this.newSpeed = s;
    }

    @Override
    public void run() {
        try {
            while (!nearCrossroad()) {
                controller.speedCheck(this);
                moveForward(getCurrentSpeed());
                Thread.sleep(40);
            }

            controller.enter(this);

            while (nearCrossroad()) {
                controller.speedCheck(this);
                moveInside(getCurrentSpeed());
                Thread.sleep(40);
            }
            controller.leave(this);

            while( onScene()) {
                controller.speedCheck(this);
                moveForward(getCurrentSpeed());
                Thread.sleep(40);
            }
            
            controller.remove(this);
            

        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    private boolean nearCrossroad() {
        return x >= 225 && x <= 355 && y >= 225 && y <= 355;
    }

    private boolean onScene() {
        return x >= -40 && x <= 640 && y >= -40 && y <= 640;
    }


    private void moveForward(int s) {
        switch (currentRoadIndex) {
            case 0 -> y += s; // north
            case 1 -> x -= s; // east
            case 2 -> y -= s; // south
            case 3 -> x += s; // west
        }
    }

    private void moveInside(int s) {
        switch (currentRoadIndex) {
            case 0 -> { // north
                if (turnDirection == -1) { x -= s; y += s; } // right turn
                else if (turnDirection == 1) { x += s; y += s; } // left turn
                else y += s; // straight
            }
            case 1 -> { // east
                if (turnDirection == -1) { x -= s; y -= s; } // right turn
                else if (turnDirection == 1) { x -= s; y += s; } // left turn
                else x -= s; // straight
            }
            case 2 -> { // south
                if (turnDirection == -1) { x += s; y -= s; } // right turn
                else if (turnDirection == 1) { x -= s; y -= s; } // left turn
                else y -= s; // straight
            }
            case 3 -> { // west
                if (turnDirection == -1) { x += s; y += s; } // right turn
                else if (turnDirection == 1) { x += s; y -= s; } // left turn
                else x += s; // straight
            }
        }
    }

    public void draw(Graphics2D g) {
        g.setColor(Color.RED);
        g.fillRect(x, y, 20, 20);

        g.setColor(Color.ORANGE);
        
        switch (turnDirection) {
            case -1 -> { // right turn
                switch (currentRoadIndex) {
                    case 0 -> g.fillRect(x, y + 10, 6, 6); // for north
                    case 2 -> g.fillRect(x + 14, y + 4, 6, 6); // for south
                    
                    case 1 -> g.fillRect(x + 4, y, 6, 6); // for east
                    case 3 -> g.fillRect(x + 10, y + 14, 6, 6); // for west
                }
            }
            case 1 -> {
                switch (currentRoadIndex) {
                    case 0 -> g.fillRect(x + 14, y + 10, 6, 6); // for north
                    case 2 -> g.fillRect(x, y + 4, 6, 6); // for south

                    case 1 -> g.fillRect(x + 4, y + 14, 6, 6); // for east
                    case 3 -> g.fillRect(x + 10, y, 6, 6); // for west
                }
            }
            default -> {} // straight
        }
    }
}