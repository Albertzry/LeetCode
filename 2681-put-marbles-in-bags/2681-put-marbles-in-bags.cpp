class Solution {
public:
    long long putMarbles(vector<int> &wt, int k) {
        int n = wt.size();
        for (int i = 0; i < n - 1; ++i)
            wt[i] += wt[i + 1];
        sort(wt.begin(), wt.end() - 1); // 相当于去掉最后一个数
        long ans = 0;
        for (int i = 0; i < k - 1; ++i)
            ans += wt[n - 2 - i] - wt[i];
        return ans;
    }
};

