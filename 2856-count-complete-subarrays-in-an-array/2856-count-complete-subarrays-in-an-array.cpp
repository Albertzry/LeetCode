class Solution {
public:
    int countCompleteSubarrays(vector<int>& nums) {
        unordered_map<int, int> map;
        for (int num : nums) {
            map[num]++;
        }
        int n = map.size();
        int l = 0, r = 0, rc = 0, ans = 0;
        unordered_map<int, int> map2;

        while (l < nums.size()) {
            while (r < nums.size() && rc < n) {
                map2[nums[r]]++;
                if (map2[nums[r]] == 1) {
                    rc++;
                }
                r++;
            }
            if (rc >= n) {
                ans += (nums.size() - r + 1); 
            }
            map2[nums[l]]--;
            if (map2[nums[l]] == 0) {
                rc--;
            }
            l++;
        }
        return ans;
    }
};