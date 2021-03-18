class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        duplicate=set()
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]<0:
                    j+=1
                elif nums[i]+nums[j]+nums[k]==0:
                    temp=[]
                    temp.extend([nums[i],nums[j],nums[k]])
                    temp.sort()
                    if tuple(temp) not in duplicate:
                        result.append(temp)
                        duplicate.add(tuple(temp))
                    j+=1
                    k-=1
                    
                else:
                    k-=1
        return result
                    
            
                
                    
                
        