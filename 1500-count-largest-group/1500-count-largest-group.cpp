class Solution {
public:
    int countLargestGroup(int n) {
        unordered_map<int,int> map;
        for(int i=1;i<=n;i++){
            int ans=0;
            int t=i;
            while(t!=0){
                ans+=(t%10);
                t/=10;
            }
            map[ans]++;
        }
        unordered_map<int,int> rc;
        int maxn=0;
        for(auto pair:map){
            maxn=max(maxn,pair.second);
            rc[pair.second]++;
        }
        return rc[maxn];
    }
};