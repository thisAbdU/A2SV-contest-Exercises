import java.util.HashMap;
import java.util.Map;

public class DoNotBeDistracted{
    public boolean checkIfDistracted(int number, String task){
        char[] toArr = task.toCharArray();
        Map<Character,Integer> mapCharacter = new HashMap<>();
        int count = 0;

        for (int i = 0; i < toArr.length - 1; i++) {
            if(mapCharacter.containsKey(toArr[i]) && (int)toArr[i] != (int)toArr[i+1]){
                mapCharacter.getOrDefault(toArr[i], count++);
            }
            else{
                mapCharacter.put(toArr[i], count);
            }
        }
        System.out.println(mapCharacter);
        return true;
    }
}