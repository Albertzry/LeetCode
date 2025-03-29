class Solution {
public:
    int minimumIndex(vector<int>& nums) {
        unordered_map<int,int> map;
        int max_e,max_f=0;
        for(int num :nums){
            map[num]++;
            if(map[num]>max_f){
                max_f=map[num];
                max_e=num;
            }
        }
        int cnt=0;
        int n=nums.size();
        for(int i=0;i<n;i++){
            if(nums[i]==max_e){
                cnt++;
            }
            if( cnt*2>(i+1) && (max_f-cnt)*2>(n-i-1)){
                return i;
            }
        }
        return -1;
    }
};