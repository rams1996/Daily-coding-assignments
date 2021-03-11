class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        smallest=float('inf')
        for i in range(len(nums)):
            smallest=min(smallest,nums[i])
            for j in range(i+1,len(nums)):
                if smallest<nums[j]<nums[i]:
                    return True
        return False
            
            
        