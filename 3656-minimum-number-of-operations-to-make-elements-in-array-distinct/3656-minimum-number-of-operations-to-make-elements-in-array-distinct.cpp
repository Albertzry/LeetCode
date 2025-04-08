class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int ans=0;
        while(!nums.empty()&&true){
            unordered_map<int,int> rc;
            bool judge=true;
            for(int n:nums){
                if(rc[n]>=1){
                    judge=false;
                    break;
                }else{
                    rc[n]++;
                }
            }
            if(judge==false){
                ans++;
                int i=3;
                while(i>0&&!nums.empty()){
                    nums.erase(nums.begin());
                    i--;
                }
            }else{
                break;
            }
        }
        return ans;
    }
};