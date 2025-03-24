class Solution {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        ranges::sort(meetings); // 按照左端点从小到大排序
        int start = 1, end = 0; // 当前合并区间的左右端点
        for (auto& p : meetings) {
            if (p[0] > end) { // 不相交
                days -= end - start + 1; // 当前合并区间的长度
                start = p[0]; // 下一个合并区间的左端点
            }
            end = max(end, p[1]);
        }
        days -= end - start + 1; // 最后一个合并区间的长度
        return days;
    }
};
