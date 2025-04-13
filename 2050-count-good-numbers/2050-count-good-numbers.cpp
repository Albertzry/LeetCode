class Solution {
    const int MOD = 1'000'000'007;

    long long qpow(long long x, long long n) {
        long long res = 1;
        while (n) {
            if (n & 1) {
                res = res * x % MOD;
            }
            x = x * x % MOD;
            n >>= 1;
        }
        return res;
    }

public:
    int countGoodNumbers(long long n) {
        return qpow(5, (n + 1) / 2) * qpow(4, n / 2) % MOD;
    }
};

