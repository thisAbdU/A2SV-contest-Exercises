class Solution {

    public int maxConsecutiveAnswers(String answerKey, int k) {
        
        int max1 = findMaxConsecutiveLength(answerKey,'T',k);
        int max2 = findMaxConsecutiveLength(answerKey,'F',k);
        
        return Math.max(max1,max2);
    }
    
    public int findMaxConsecutiveLength(String str,char ch,int k){
        int i=-1;
        int j=-1;
        int n=str.length();
        
        int max=0;
        int cnt=0;
        
        while(true){
            boolean f1=true;
            boolean f2=true;
            
            while(i<n-1 && cnt<=k){                 // acquisition of elements in window untill count<=k
                max=Math.max(max,i-j);
                
                if(str.charAt(++i)==ch){
                    cnt++;
                }
                
                f1=false;
            }
            
            while(cnt>k){                          //  release of elements in window untill count<=k
                j++;
                
                if(str.charAt(j)==ch){
                    cnt--;
                }
                
                f2=false;
            }
            
            if(f1 && f2){
                break;
            }
        }
        
        max=Math.max(max,i-j);
        
        return max;
    }
}