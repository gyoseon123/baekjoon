#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int main() {
    int t;
    cin >> t;

    for (int test = 0; test < t; ++test) {
        int n, s, e;
        cin >> n >> s >> e;
        vector<int> l(n);
        for (int i = 0; i < n; ++i) {
            cin >> l[i];
        }

        vector<int> pl(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pl[i + 1] = pl[i] + l[i];
        }

        vector<pair<int, int>> arr;
        int cnt = 1;
        int tmp = l[0];
        for (int i = 1; i < n; ++i) {
            if (l[i] == tmp) {
                cnt += 1;
            } else {
                if (tmp == 1) {
                    arr.push_back({i - cnt, i - 1});
                }
                cnt = 1;
                tmp = l[i];
            }
        }
        if (l[n - 1] == 1) {
            arr.push_back({n - cnt, n - 1});
        }

        if (arr.size() <= 1) {
            cout << "Case #" << test + 1 << endl;
            cout << 0 << endl;
            continue;
        }

        int ans = INT_MAX;

        int left = arr[0].second;
        int right = arr.back().second;
        int cnt1 = pl[right + 1] - pl[left + 1];
        int cnt0 = right - left - cnt1;

        int minn = min(cnt0 * s, cnt1 * e);
        ans = min(minn, ans);

        left = arr[0].first;
        right = arr.back().first;
        cnt1 = pl[right + 1] - pl[left + 1];
        cnt0 = right - left - cnt1;

        minn = min(cnt0 * s, cnt1 * e);
        ans = min(minn, ans);

        for (size_t i = 1; i < arr.size() - 1; ++i) {
            int ret = 0;

            left = arr[0].first;
            right = arr[i].first;
            cnt1 = pl[right + 1] - pl[left + 1];
            cnt0 = right - left - cnt1;

            minn = min(cnt0 * s, cnt1 * e);
            ret += minn;

            left = arr[i].second;
            right = arr.back().second;
            cnt1 = pl[right + 1] - pl[left + 1];
            cnt0 = right - left - cnt1;

            minn = min(cnt0 * s, cnt1 * e);
            ret += minn;

            ans = min(ret, ans);
        }

        cout << "Case #" << test + 1 << endl;
        cout << ans << endl;
    }

    return 0;
}
