class Solution {
public:
    struct Node {
        int x, y, d;
        bool operator<(const Node& other) const {
            return d > other.d;
        }
    };

    static constexpr int directions[] = {0, 1, 0, -1, 0};

    vector<int> maxPoints(const vector<vector<int>>& grid, const vector<int>& queries) {
        const int m = grid.size(), n = grid[0].size();
        vector<int> distance(m * n, INT_MAX);
        priority_queue<Node> pq;
        map<int, int> cnt;
        distance[0] = grid[0][0];
        pq.push({0, 0, grid[0][0]});
        while (!pq.empty()) {
            const auto [x, y, d] = pq.top();
            pq.pop();
            if (d > distance[n * x + y])
                continue;
            ++cnt[d];
            for (int i = 0;i < 4;++i) {
                const int nx = x + directions[i];
                const int ny = y + directions[i + 1];
                if (nx < 0 || ny < 0 || m <= nx || n <= ny) continue;
                const int nd = max(d, grid[nx][ny]);
                if (nd < distance[n * nx + ny]) {
                    distance[n * nx + ny] = nd;
                    pq.push({nx, ny, nd});
                }
            }
        }
        int sum = 0;
        for (auto& [k, v] : cnt)
            v = sum += v;
        vector<int> ans;
        for (int e : queries) {
            const auto it = cnt.lower_bound(e);
            ans.push_back(it != cnt.begin() ? prev(it)->second : 0);
        }
        return ans;
    }
};
