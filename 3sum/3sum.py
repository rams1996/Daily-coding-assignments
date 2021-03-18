class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        i=0
        while i<len(nums):
            while i!=0 and i<len(nums) and nums[i]==nums[i-1]:
                i+=1
            left=i+1
            right=len(nums)-1
            
            while left<right:
                
                while left<right and left!=i+1 and nums[left]==nums[left-1]:
                    left+=1
                while left<right and right!=len(nums)-1 and nums[right]==nums[right+1]:
                    right-=1
                if left<right:
                    if nums[i]+nums[left]+nums[right]==0:
                        result.append([nums[i],nums[left],nums[right]])
                        left+=1
                        right-=1
                    elif nums[i]+nums[left]+nums[right]>0:
                        right-=1
                    else:
                        left+=1
            i+=1
        return result
            
        