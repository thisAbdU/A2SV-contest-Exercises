class Solution {
    public int maxVowels(String s, int k) {
        int currentNoVowels = 0;
        int maxNoVowels = 0;
        int length_count = 0;
        
        for(int i=0; i < s.length(); i++){
            length_count++;
            while(length_count > k){
                if (s.charAt(i-length_count + 1) == 'a' ||s.charAt(i-length_count + 1) == 'e'||s.charAt(i-length_count + 1) == 'i' ||s.charAt(i-length_count + 1) == 'o'|| s.charAt(i-length_count + 1) == 'u' ){
                currentNoVowels--;
            }
                length_count--;
            }
            if (s.charAt(i) == 'a' || s.charAt(i) == 'e'||s.charAt(i) == 'i'||s.charAt(i) == 'o'|| s.charAt(i) == 'u'){
                currentNoVowels++;
                maxNoVowels = Math.max(maxNoVowels, currentNoVowels);
            }
        }
      return maxNoVowels;
    }
}