#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> tree;

int sum_q(int node, int start, int end, int left, int right) {
    if (left <= start && end <= right) return tree[node];
    if (right < start || end < left) return 0;
    int mid = (start + end) / 2;
    return sum_q(node * 2, start, mid, left, right) + sum_q(node * 2 + 1, mid + 1, end, left, right);
}

void update_q(int node, int start, int end, int idx, int diff) {
    if (start <= idx && idx <= end) {
        tree[node] += diff;
        if (start != end) {
            int mid = (start + end) / 2;
            update_q(node * 2, start, mid, idx, diff);
            update_q(node * 2 + 1, mid + 1, end, idx, diff);
        }
    }
}

int main() {
    int n;
    cin >> n;
    
    vector<int> l(n);
    for (int i = 0; i < n; ++i) {
        cin >> l[i];
    }
    
    tree.resize(4 * n, 0);
    
    vector<pair<int, int>> arr;
    for (int i = 0; i < n; ++i) {
        arr.push_back({l[i], i});
    }
    
    sort(arr.begin(), arr.end());
    
    long long ans = 0;
    
    for (int i = 0; i < n; ++i) {
        int now = arr[i].first;
        int idx = arr[i].second;
        ans += sum_q(1, 0, n - 1, idx + 1, n - 1);
        update_q(1, 0, n - 1, idx, 1);
    }
    
    cout << ans << endl;
    
    return 0;
}
