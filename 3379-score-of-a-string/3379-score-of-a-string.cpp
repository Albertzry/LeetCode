class Solution {
public:
    int scoreOfString(string s) {
        int ans=0;
        int l=s.length();
        for(int i=0;i<l-1;i++){
            ans+=abs(s[i]-s[i+1]);
        }
        return ans;
    }
};