class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        int n=nums.size();
        if(nums.front()<k){
            return -1;
        }
        vector<int> rc;
        for(int i=0;i<n;i++){
            if(rc.empty()||!rc.empty()&&rc.back()!=nums[i]){
                rc.push_back(nums[i]);
            }
        }
        if(nums.front()==k){
            return rc.size()-1;
        }
        return rc.size();
    }
};