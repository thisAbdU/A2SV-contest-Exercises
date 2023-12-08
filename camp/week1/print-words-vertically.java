import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<String> printVertically(String s) {
        List<String> transposed = new ArrayList<>();
        String[] words = s.split("\\s+"); // Split the input string into words

        // Find the maximum length among all words
        int maxLength = 0;
        for (String word : words) {
            maxLength = Math.max(maxLength, word.length());
        }

        // Initialize the transposed list with empty strings
        for (int i = 0; i < maxLength; i++) {
            transposed.add("");
        }

        // Populate the transposed list
        for (String word : words) {
            for (int i = 0; i < maxLength; i++) {
                if (i < word.length()) {
                    transposed.set(i, transposed.get(i) + word.charAt(i));
                } else {
                    transposed.set(i, transposed.get(i) + " ");
                }
            }
        }

        return trimRight(transposed);
    }

    // Trim right for each string in the list
    private static List<String> trimRight(List<String> list) {
        List<String> trimmedList = new ArrayList<>();
        for (String str : list) {
            trimmedList.add(str.replaceAll("\\s+$", ""));
        }
        return trimmedList;
    }
}
