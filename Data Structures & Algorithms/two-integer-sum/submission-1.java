class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] rs = new int[2];
        for(int i = 0; i < nums.length; i++){
            map.put(nums[i], i);
        }
        for(int i = 0; i < nums.length; i++){
            int diff = target - nums[i];
            if(map.containsKey(diff) && map.get(diff) != i){
                int value = map.get(diff);
                rs[0] = i;
                rs[1] = value;
                return rs;
            }
            
        }
        return rs;
    }
}
