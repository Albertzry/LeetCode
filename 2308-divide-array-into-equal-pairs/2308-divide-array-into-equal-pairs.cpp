class Solution {
public:
    bool divideArray(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int i=0;
        while(i<nums.size()){
            if(nums[i]!=nums[i+1]){
                return false;
            }
            i+=2;
        }
        return true;
    }
};