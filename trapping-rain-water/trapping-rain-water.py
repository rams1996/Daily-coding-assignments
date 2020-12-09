class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftMax=[]
        rightMax=[]
        maxUntilNow=0
        for i in range(len(height)):
            maxUntilNow=max(maxUntilNow,height[i])
            leftMax.append(maxUntilNow)
        maxUntilNow=0
        for i in range(len(height)-1,-1,-1):
            maxUntilNow=max(maxUntilNow,height[i])
            rightMax.append(maxUntilNow)
        # print(leftMax,rightMax)
        rightMax=rightMax[::-1]
        total=0
        for i in range(1,len(leftMax)):
            # if min(leftMax[i],rightMax[i])>height[i]:
            total+=min(leftMax[i],rightMax[i]) -height[i]
        return total
            
        
