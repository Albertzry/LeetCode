class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        int m = grid.size();
        int n = grid[0].size();
        vector<int> elements;

        // 将网格中的所有元素存入一个一维数组
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                elements.push_back(grid[i][j]);
            }
        }

        // 检查所有元素与第一个元素的差是否是 x 的倍数
        int first = elements[0];
        for (int num : elements) {
            if ((num - first) % x != 0) {
                return -1;
            }
        }

        // 排序
        sort(elements.begin(), elements.end());

        // 选择中位数作为目标值
        int target = elements[elements.size() / 2];

        // 计算操作次数
        int operations = 0;
        for (int num : elements) {
            operations += abs(num - target) / x;
        }

        return operations;
    }
};

