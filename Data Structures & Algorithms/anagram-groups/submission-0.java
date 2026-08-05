class Solution {
    public static boolean isAnagram(String s1, String s2){
        if(s1.length() != s2.length()) return false;
        char[] a = s1.toCharArray();
        char[] b = s2.toCharArray();
        Arrays.sort(a);
        Arrays.sort(b);
        return Arrays.equals(a, b);
    }
    public List<List<String>> groupAnagrams(String[] strs) {
        List<String> list = new ArrayList<>(Arrays.asList(strs));
        List<List<String>> rs = new ArrayList<>();

        while(!list.isEmpty()){
            // Take the first element and make a new list
            String firstWord = list.remove(0);
            List<String> group = new ArrayList<>();
            group.add(firstWord);

            // Find anagrams in the remain list
            Iterator<String> iterator = list.iterator();
            while (iterator.hasNext()) {
                String s = iterator.next();
                if(isAnagram(firstWord, s)){
                    group.add(s);
                    iterator.remove();
                }
            }
            rs.add(group);
        }
        return rs;
    }
}
