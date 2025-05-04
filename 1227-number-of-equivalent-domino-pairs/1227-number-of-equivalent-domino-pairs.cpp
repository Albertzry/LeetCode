class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        unordered_map<int, int> countMap;
        for (auto& domino : dominoes) {
            sort(domino.begin(), domino.end());
            int key = domino[0] * 10 + domino[1];
            countMap[key]++;
        }
        int ans = 0;
        for (auto& pair : countMap) {
            ans += (pair.second * (pair.second - 1)) / 2;
        }
        return ans;
    }
};