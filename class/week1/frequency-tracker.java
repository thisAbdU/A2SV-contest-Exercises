import java.util.HashMap;
import java.util.Map;

public class FrequencyTracker {

    Map<Integer, Integer> numFrequency = new HashMap<>();
    Map<Integer, Integer> metaFrequency = new HashMap<>();

    public void add(int number) {
        int prevFrequency = numFrequency.getOrDefault(number, 0);
        numFrequency.put(number, prevFrequency + 1);
        
        // Update meta-frequency map
        metaFrequency.put(prevFrequency, metaFrequency.getOrDefault(prevFrequency, 0) - 1);
        metaFrequency.put(prevFrequency + 1, metaFrequency.getOrDefault(prevFrequency + 1, 0) + 1);
    }

    public void deleteOne(int number) {
        if (numFrequency.containsKey(number)) {
            int frequency = numFrequency.get(number);
            
            // Update meta-frequency map
            metaFrequency.put(frequency, metaFrequency.getOrDefault(frequency, 0) - 1);
            if (frequency - 1 > 0) {
                metaFrequency.put(frequency - 1, metaFrequency.getOrDefault(frequency - 1, 0) + 1);
            }
            
            // Update frequency map
            numFrequency.put(number, frequency - 1);
            
            if (frequency - 1 == 0) {
                numFrequency.remove(number);
            }
        }
    }

    public boolean hasFrequency(int frequency) {
        return metaFrequency.containsKey(frequency) && metaFrequency.get(frequency) > 0;
    }
}
