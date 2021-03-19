class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearchLeft(low,high):
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    if mid==0 or nums[mid]!=nums[mid-1]:
                        return mid
                    else:
                        high=mid-1
                    
                elif nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
        def binarySearchRight(low,high):
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    if mid==len(nums)-1 or nums[mid+1]>nums[mid]:
                        return mid
                    else:
                        low=mid+1
                    
                elif nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
        
        
        
        
        
        if not nums or len(nums)==0:
            return [-1,-1]
        left=binarySearchLeft(0,len(nums)-1)
        
        right=binarySearchRight(0,len(nums)-1)
        if left==None:
            return [-1,-1]
        return [left,right]
        