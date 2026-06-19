class Solution {
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> res = new ArrayList<>();

        int one = 0;
        int countOne = 0;
        int two = 0;
        int countTwo = 0;

        for (int num : nums) {
            if (num == one) {
                countOne++;
            } else if (num == two) {
                countTwo++;
            } else if (countOne == 0) {
                one = num;
                countOne = 1;
            } else if (countTwo == 0) {
                two = num;
                countTwo = 1;
            } else {
                countOne--;
                countTwo--;
            }
        }

        int count1 = 0;
        int count2 = 0;
        for (int num : nums) {
            if (num == one) count1++;
            else if (num == two) count2++;
        }
        
        int target = (int) (nums.length / 3);
        if (count1 > target) res.add(one);
        if (count2 > target) res.add(two);
        return res;
    }
}