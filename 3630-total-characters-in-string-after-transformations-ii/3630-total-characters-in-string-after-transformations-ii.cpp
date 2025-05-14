class Solution {
    static constexpr int MOD = 1'000'000'007;
    static constexpr int SIZE = 26;

    using Matrix = array<array<int, SIZE>, SIZE>;

    Matrix mul(Matrix& a, Matrix& b) {
        Matrix c{};
        for (int i = 0; i < SIZE; i++) {
            for (int k = 0; k < SIZE; k++) {
                if (a[i][k] == 0) {
                    continue;
                }
                for (int j = 0; j < SIZE; j++) {
                    c[i][j] = (c[i][j] + (long long) a[i][k] * b[k][j]) % MOD;
                }
            }
        }
        return c;
    }

    Matrix pow(Matrix a, int n) {
        Matrix res = {};
        for (int i = 0; i < SIZE; i++) {
            res[i][i] = 1; 
        }
        while (n) {
            if (n & 1) {
                res = mul(res, a);
            }
            a = mul(a, a);
            n >>= 1;
        }
        return res;
    }

public:
    int lengthAfterTransformations(string s, int t, vector<int>& nums) {
        Matrix m{};
        for (int i = 0; i < SIZE; i++) {
            for (int j = i + 1; j <= i + nums[i]; j++) {
                m[i][j % SIZE] = 1;
            }
        }
        Matrix mt = pow(m, t);

        int cnt[SIZE]{};
        for (char c : s) {
            cnt[c - 'a']++;
        }

        long long ans = 0;
        for (int i = 0; i < SIZE; i++) {
            ans += reduce(mt[i].begin(), mt[i].end(), 0LL) * cnt[i];
        }
        return ans % MOD;
    }
};
