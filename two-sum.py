class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        value={}
        
        for i in range(len(nums)):
            if target-nums[i] in value:
                return [i,value[target-nums[i]]]
            else:
                value[nums[i]]=i
        return -1
        
