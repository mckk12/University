import java.util.*;
import java.util.concurrent.CopyOnWriteArrayList;

public class TrafficController {

    public final List<Car> cars = new CopyOnWriteArrayList<>();
    private final List<Car> waiting = new ArrayList<>();
    private final Set<Car> inside = new HashSet<>();

    private boolean isDeadlock() {
        if (waiting.size() < 4) return false;

        Set<Integer> indices = new HashSet<>();
        for (Car c : waiting) {
            indices.add(c.currentRoadIndex);
        }
        return indices.contains(0) && indices.contains(1) && indices.contains(2) && indices.contains(3);
    }

    public void speedCheck(Car car) throws InterruptedException {
        for (Car other : cars) {
            if (other == car || car.currentRoadIndex != other.currentRoadIndex) continue;

            switch (car.currentRoadIndex) {
            case 0 -> {
                if (Math.abs(other.getY() - car.getY()) < 30 && other.getY() > car.getY()){
                    car.changeSpeed(other.getCurrentSpeed());
                    return;
                }
            }
            case 2 -> {
                if (Math.abs(car.getY() - other.getY()) < 30 && other.getY() < car.getY()){
                    car.changeSpeed(other.getCurrentSpeed());
                    return;
                }
            }
            case 1  -> {
                if (Math.abs(car.getX() - other.getX()) < 30 && other.getX() < car.getX()){
                    car.changeSpeed(other.getCurrentSpeed());
                    return;
                }
            }
            case 3  -> {
                if (Math.abs(other.getX() - car.getX()) < 30 && other.getX() > car.getX()){
                    car.changeSpeed(other.getCurrentSpeed());
                    return;
                }
            }
            default -> {}
            }
        }

        car.changeSpeed(-1);
        
    }

    public synchronized void enter(Car car) throws InterruptedException {
        waiting.add(car);
        car.changeSpeed(0);
        Thread.sleep(250);

        while (true) {
            boolean canEnter = true;

            // zasada prawej ręki
            for (Car other : waiting) {
                if (other == car) continue;
                if ((other.currentRoadIndex + 1) % 4 == car.currentRoadIndex) {
                    canEnter = false;
                }
            }

            // kolizje
            if (!inside.isEmpty()) {
                for (Car other : inside) {
                    int c1 = car.currentRoadIndex;
                    int t1 = car.turnDirection;
                    int c2 = other.currentRoadIndex;
                    int t2 = other.turnDirection;

                    boolean collision =
                            ((t1 == 1 && t2 == 1) || // both left
                            (t1 == 1 && t2 == 0) || // one left, one straight
                            (t1 == 0 && t2 == 1) || // one straight, one left
                            (t1==0 && t2==-1 && (c2+1)%4!= c1) || // one straight, one right
                            (t1==-1 && t2==0 && (c1+1)%4!= c2) || // one right, one straight
                            (t1==0 && t2==0 && (c1+2)%4!= c2 ) || // both straight
                            (t1==1 && t2==-1 && !((c1+1)%4==c2)) || // one left, one right
                            (t1==-1 && t2==1 && !((c2+1)%4==c1)))  // one right, one left
                            && c1!=c2; 
                    if (collision) {
                        canEnter = false;
                    }
                }
            }

            // deadlock – przepuszczamy ostatniego przybyłego
            if (isDeadlock()) {
                if (car == waiting.get(waiting.size()-1)) {
                    canEnter = true;
                }
            }

            if (canEnter) break;

            wait();
        }

        waiting.remove(car);
        inside.add(car);
    }

    public synchronized void leave(Car car) {
        car.changeSpeed(car.getOldSpeed());
        inside.remove(car);
        car.currentRoadIndex = (car.currentRoadIndex - car.turnDirection + 4) % 4;
        car.turnDirection = 0;
        notifyAll();
    }

    public synchronized void remove(Car car) {
        cars.remove(car);
        notifyAll();
    }

}
