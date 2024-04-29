import java.util.ArrayList;

class MyCircularQueue {
    ArrayList<Integer> circularQueue;
    int len_;
    public MyCircularQueue(int k) {
        circularQueue = new ArrayList<>();
        len_ = k;
    }
    
    public boolean enQueue(int value) {
        if(circularQueue.size() < len_){
            circularQueue.add(value);
            return true;
        }
        return false;
    }
    
    public boolean deQueue() {
        if(circularQueue.size() > 0){
            circularQueue.removeFirst();
            return true;
        }
        return false;
    }
    
    public int Front() {
        if(circularQueue.size() > 0){
            return circularQueue.get(0);
        }
        return -1;
    }
    
    public int Rear() {
        if(circularQueue.size() > 0){
            return circularQueue.get(circularQueue.size() - 1);
        }
        return -1;
    }
    
    public boolean isEmpty() {
        return circularQueue.size() == 0;
    }
    
    public boolean isFull() {
        return circularQueue.size() == len_;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */