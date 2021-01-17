class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        HashSet<List<Integer>> res = new HashSet<>();
        List<Integer> l1 = new ArrayList<>();
        for (int i = 0; i< nums.length - 2; i++)
        {
            int a = nums[i];
            int start = i + 1;
            int end = nums.length - 1;
            while (start < end)
            {
                int b = nums[start];
                int c = nums[end];
                if (a + b + c == 0)
                {
                    res.add(Arrays.asList(a, b, c));
                    start = start + 1;
                    end = end - 1;
                }
                else if (a + b + c > 0)
                    end = end - 1;
                else
                    start = start + 1;
            }
            res.add(l1);
        }
        List<List<Integer>> res1 = new ArrayList<>();
        for(List<Integer> l2: res)
        {
            if(l2.size() != 0)
                res1.add(l2);
        }
        return res1;
    }
}
