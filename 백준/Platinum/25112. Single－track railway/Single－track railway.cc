#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>

#define int long long

using namespace std;

int tree[808080];
int l[202020];
int suml = 0;
int n;

int init(int node, int start, int end) {
    if (start == end) {
        tree[node] = l[start];
        return tree[node];
    } else {
        int mid = (start + end) / 2;
        tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end);
        return tree[node];
    }
}

int sum_query(int node, int start, int end, int left, int right) {
    if (start > right || end < left)
        return 0;

    if (start >= left && end <= right)
        return tree[node];

    int mid = (start + end) / 2;
    return sum_query(node * 2, start, mid, left, right) + sum_query(node * 2 + 1, mid + 1, end, left, right);
}

void update_query(int node, int start, int end, int index, int diff) {
    if (index >= start && index <= end) {
        tree[node] += diff;
        if (start != end) {
            int mid = (start + end) / 2;
            update_query(node * 2, start, mid, index, diff);
            update_query(node * 2 + 1, mid + 1, end, index, diff);
        }
    }
}

int f(int now) {
    return abs(suml - sum_query(1, 0, n - 1, 0, now) * 2);
}

int search() {
    int lo = 0;
    int hi = n + 1;

    while (hi - lo >= 3) {
        int p = (lo * 2 + hi) / 3;
        int q = (lo + hi * 2) / 3;

        if (f(p) >= f(q)) {
            lo = p;
        } else {
            hi = q;
        }
    }

    int ret = 1e9;
    for (int i = lo; i <= hi; ++i) {
        ret = min(ret, f(i));
    }

    return ret;
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n;

    for (int i = 1; i < n; ++i) {
        cin >> l[i];
    }
    n++;
    suml = 0;
    for (int i = 1; i < n; i++) suml += l[i];

    init(1, 0, n - 1);

    cout << search() << '\n';

    int k;
    cin >> k;

    for (int i = 0; i < k; ++i) {
        int a, b;
        cin >> a >> b;
        int diff = b - l[a];
        suml += diff;
        l[a] = b;
        update_query(1, 0, n - 1, a, diff);
        cout << search() << '\n';
    }

    return 0;
}
