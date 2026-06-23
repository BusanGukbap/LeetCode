class Solution {
public:
    int zigZagArrays(int n, int l, int r) {
        const long long MOD = 1000000007;
        int m = r - l + 1;

        if (n == 1) return m;

        vector<long long> up(m + 1), down(m + 1);

        for (int v = 1; v <= m; v++) {
            up[v] = v - 1;
            down[v] = m - v;
        }

        for (int len = 3; len <= n; len++) {
            vector<long long> nu(m + 1), nd(m + 1);

            long long pref = 0;
            for (int v = 1; v <= m; v++) {
                nu[v] = pref;
                pref = (pref + down[v]) % MOD;
            }

            long long suff = 0;
            for (int v = m; v >= 1; v--) {
                nd[v] = suff;
                suff = (suff + up[v]) % MOD;
            }

            up.swap(nu);
            down.swap(nd);
        }

        long long ans = 0;
        for (int v = 1; v <= m; v++) {
            ans = (ans + up[v] + down[v]) % MOD;
        }
        return ans;
    }
};