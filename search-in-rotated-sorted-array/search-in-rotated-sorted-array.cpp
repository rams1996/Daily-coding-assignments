class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        int low=0;
        int high=nums.size()-1;
        while(low<=high){
            
            int mid=high+(low-high)/2;
            if(target==nums[mid]){
                    return mid;
                }
            else if (nums[low]<=nums[mid]){
                if((target>=nums[low])&&(target<nums[mid])){
                    high=mid-1;
                }
                else{
                    low=mid+1;
                }
            }
            else{
                if(target>nums[mid] && target<=nums[high]){
                    low=mid+1;
                }
                else{
                    high=mid-1;
                }
            }
        }
        return -1;
        
    }
};