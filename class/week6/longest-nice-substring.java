import java.util.HashSet;
import java.util.Set;

public class Solution {
    public static void main(String[] args) {
        String result = new Solution().longestNiceSubstring("abABB");
        System.out.println(result);
    }

    public String longestNiceSubstring(String s) {
        int[] sub = longestNiceSubstring(s, 0, s.length());
        return s.substring(sub[0], sub[1]);
    }

    private int[] longestNiceSubstring(String s, int left, int right) {
        Set<Character> charSet = getCharSet(s, left, right);

        for (int i = left; i < right; i++) {
            if (!charSet.contains(Character.toLowerCase(s.charAt(i)))
                    || !charSet.contains(Character.toUpperCase(s.charAt(i)))) {

                int[] prefix = longestNiceSubstring(s, left, i);
                int[] suffix = longestNiceSubstring(s, i + 1, right);
                return prefix[1] - prefix[0] >= suffix[1] - suffix[0]
                        ? prefix
                        : suffix;
            }
        }

        return new int[]{left, right};
    }

    private Set<Character> getCharSet(String s, int left, int right) {
        Set<Character> charSet = new HashSet<>();

        for (int i = left; i < right; i++)
            charSet.add(s.charAt(i));

        return charSet;
    }
}
