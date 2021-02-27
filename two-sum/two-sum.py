class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        
        hmap={}
        
        for j,i in enumerate(nums):
            if target-i in hmap:
                return [j,hmap[target-i]]
            else:
                hmap[i]=j
        
        