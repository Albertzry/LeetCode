class Solution {
    vector<vector<pair<int, int>>> g;
    vector<int> cc_and, ids;

    int dfs(int x) {
        ids[x] = cc_and.size(); 
        int and_ = -1;
        for (auto &[y, w]: g[x]) {
            and_ &= w;
            if (ids[y] < 0) { 
                and_ &= dfs(y);
            }
        }
        return and_;
    }

public:
    vector<int> minimumCost(int n, vector<vector<int>> &edges, vector<vector<int>> &query) {
        g.resize(n);
        for (auto &e: edges) {
            int x = e[0], y = e[1], w = e[2];
            g[x].emplace_back(y, w);
            g[y].emplace_back(x, w);
        }

        ids.resize(n, -1); 
        for (int i = 0; i < n; i++) {
            if (ids[i] < 0) { 
                cc_and.push_back(dfs(i)); 
            }
        }

        vector<int> ans;
        ans.reserve(query.size()); 
        for (auto &q: query) {
            int s = q[0], t = q[1];
            ans.push_back(ids[s] != ids[t] ? -1 : cc_and[ids[s]]);
        }
        return ans;
    }
};
