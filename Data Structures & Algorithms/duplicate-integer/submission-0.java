class Solution {
    public boolean hasDuplicate(int[] nums) {
        List<Integer> list = new ArrayList<>();
        for (int i: nums) {
            list.add(i);
        }
        Collections.sort(list);
        for(int i = 0; i < list.size()-1; i++){
            if(list.get(i) - list.get(i+1) == 0) return true;
        }
        return false;
    }
}