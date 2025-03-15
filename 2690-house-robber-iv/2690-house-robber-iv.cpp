class Solution {
public:
    int minCapability(vector<int>& nums, int k) {
        int lower=*min_element(nums.begin(),nums.end());
        int upper=*max_element(nums.begin(),nums.end());
        while (lower<=upper){
            int cnt=0;
            int middle =(lower+upper)/2;
            bool judge=false;
            for (int x : nums){
                if(x<=middle&&judge==false){
                    cnt++;
                    judge=true;
                }
                else{
                    judge=false;
                }
            }
            if (cnt>=k){
                upper=middle-1;
            }
            else{
                lower=middle+1;
            }
        }
        return lower;
    }
};