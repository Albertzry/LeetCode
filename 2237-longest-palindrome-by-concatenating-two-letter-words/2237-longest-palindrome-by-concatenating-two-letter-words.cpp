class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        unordered_map<string,int> fq;
        for (auto word:words) 
            fq[word]++;
        int len = 0;
        bool mid = false;
        for(auto [word,cnt]:fq){
            string re = string{word.rbegin(), word.rend()};
            if (word!=re && fq.count(re)){
                int pairs = min(cnt,fq[re]);
                len += pairs*4;
                fq[re] -= pairs;
                fq[word] -= pairs;
            }
        }
        for(auto [word,cnt]:fq){
            if(word[0]==word[1]){
                len += (cnt/2)*4;
                if(cnt%2 && !mid){
                    len += 2;
                    mid = true;
                }
            }
        }
        return len;
    }
};