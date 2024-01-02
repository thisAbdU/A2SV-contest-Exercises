class Solution {
    public List<Integer> maxScoreIndices(int[] nums) {
        int numZeros = 0;
        for(int i = 0; i < nums.length; i++){
            numZeros += nums[i] == 0 ? 1 : 0;
        }
        Map<Integer, List<Integer>> scoreToIndex = new HashMap<>();
        int onesCount = 0;
        int maxDivScore = -1;
        
        for(int i = nums.length; i >= 0; i--){
            if(i < nums.length && nums[i] == 1){
                onesCount++;
            }else{
                numZeros--;
            }
            int currScore = onesCount + numZeros;
            if(currScore > maxDivScore){
                maxDivScore = currScore;
            }
            
            if(scoreToIndex.containsKey(currScore)){
                scoreToIndex.get(currScore).add(i);
            }else{
                List<Integer> newList = new ArrayList<>();
                newList.add(i);
                scoreToIndex.put(currScore, newList);
            }
        }
        return scoreToIndex.get(maxDivScore);
    } 
}