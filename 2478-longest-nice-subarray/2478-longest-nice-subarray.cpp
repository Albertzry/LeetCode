class Solution {
public:
    int longestNiceSubarray(vector<int>& nums) {
        int l=0,r=0,rec=0;
        int n=nums.size();
        int ans=0;
        while(r<n){
            while((rec&nums[r])!=0){
                rec^=nums[l];
                l++;
            }
            rec|=nums[r];
            ans=max(ans,r-l+1);
            r++;
        }
        return ans;
    }
};