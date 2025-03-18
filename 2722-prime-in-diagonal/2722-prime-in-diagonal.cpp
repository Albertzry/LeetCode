class Solution {
public:
    int diagonalPrime(vector<vector<int>>& nums) {
        int ans=0;
        int n=nums.size();
        for(int i=0;i<n;i++){
            if(judge(nums[i][i])){
                ans=max(ans,nums[i][i]);
            }
            if(judge(nums[i][n-i-1])){
                ans=max(ans,nums[i][n-i-1]);
            }
        }
        return ans;
    }
    bool judge(int x){
        if(x==1){
            return false;
        }
        int limit =(int)pow(x,0.5);
        for(int i=2;i<=limit;i++){
            if(x%i==0){
                return false;
            }
        }
        return true;
    }
};