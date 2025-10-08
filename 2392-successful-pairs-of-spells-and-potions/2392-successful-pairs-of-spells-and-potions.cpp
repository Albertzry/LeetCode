class Solution {
public:
    static vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        sort(potions.begin(), potions.end());
        const int n=spells.size();
        vector<int> result(n, 0);
        
        const int m=potions.size();
        const int maxPotion=potions[m-1];

        
        for (int i=0; i<n; i++) {
            int spell=spells[i];
            long long k = (success+spell-1)/spell;
            if (k<=maxPotion) {
                result[i]=m-(lower_bound(potions.begin(), potions.end(), k)-potions.begin());
            }
        }       
        return result;
    }
};