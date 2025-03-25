class Solution {
public:
    bool check(vector<pair<int, int>>& intervals) {
        ranges::sort(intervals, {}, [](auto& a) { return a.first; });// 按照左端点从小到大排序
        int cnt = 0, max_r = 0;
        for (auto& [l, r] : intervals) {
            if (l >= max_r) { // 新区间
                cnt++;
            }
            max_r = max(max_r, r); // 更新右端点最大值
        }
        return cnt >= 3; // 也可以在循环中提前退出
    }

    bool checkValidCuts(int, vector<vector<int>>& rectangles) {
        vector<pair<int, int>> a, b;
        for (auto& rect : rectangles) {
            a.emplace_back(rect[0], rect[2]);
            b.emplace_back(rect[1], rect[3]);
        }
        return check(a) || check(b);
    }
};
