int freq[100001]={0};
class Solution {
public:
    int minPairSum(vector<int>& nums) {
        // find min & max for nums at once
        auto [m, M]=minmax_element(nums.begin(), nums.end());
        int l=*m, r=*M;// set 2 pointers initially
        memset( freq+l, 0, (r-l+1)*sizeof(int));// reset freq
        for(int x: nums)
            freq[x]++;
    
        int maxP=0, rN=0, lN=0, k=nums.size()/2;

        for(int pairN=1; pairN<=k; pairN++) {

            while (lN<pairN) lN+=freq[l++];
            
            while (rN<pairN) rN+=freq[r--];
            
            maxP=max(maxP, l+r);
        }
        return maxP;
    }
};
auto init = []()
{ 
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    return 'c';
}();