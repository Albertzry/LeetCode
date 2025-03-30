class Solution {
public:
    vector<int> partitionLabels(string s) {
        vector<int> ans;
        int n=s.size();
        int start=0,last=n-1;
        while(start<n){
            char c=s[start];
            last=search(s,c);
            int i=start+1;
            while(i<last){
                last=max(last,search(s,s[i]));
                i++;
            }
            ans.push_back(last-start+1);
            start=last+1;

        }
        return ans;
    }
    int search(string s,char target){
        int n=s.size();
        int l=n-1;
        while(l>=0){
            if(s[l]==target){
                return l;
            }
            l--;
        }
        return 0;
    }
};