class Solution {
public:
    int countPaths(int n, vector<vector<int>> &roads) {
        vector<vector<long long>> g(n, vector<long long>(n, LLONG_MAX / 2)); // 邻接矩阵
        for (auto &r : roads) {
            int x = r[0], y = r[1], d = r[2];
            g[x][y] = d;
            g[y][x] = d;
        }

        vector<long long> dis(n, LLONG_MAX / 2); // 防止溢出
        dis[0] = 0;
        vector<int> f(n), done(n);
        f[0] = 1;
        while (true) {
            int x = -1;
            for (int i = 0; i < n; i++) {
                if (!done[i] && (x < 0 || dis[i] < dis[x])) {
                    x = i;
                }
            }
            if (x == n - 1) {
                // 不可能找到比 dis[n-1] 更短，或者一样短的最短路了（注意本题边权都是正数）
                return f[n - 1];
            }
            done[x] = true; // 最短路长度已确定（无法变得更小）
            for (int y = 0; y < n; y++) { // 尝试更新 x 的邻居的最短路
                long long new_dis = dis[x] + g[x][y];
                if (new_dis < dis[y]) {
                    // 就目前来说，最短路必须经过 x
                    dis[y] = new_dis;
                    f[y] = f[x];
                } else if (new_dis == dis[y]) {
                    // 和之前求的最短路一样长
                    f[y] = (f[y] + f[x]) % 1'000'000'007;
                }
            }
        }
    }
};
