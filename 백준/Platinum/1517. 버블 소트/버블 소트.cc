#include <bits/stdc++.h>
// #define ll long long
#define int long long
const int inf = 1e9;

using namespace std;

struct Seg{
    int n;
    vector<int> tree;

    Seg(int n){
        this->n = n;
        tree.resize(4*n);
    }

    void update(int node, int start, int end, int idx, int diff){
        if (end < idx || idx < start) return;
        if (start == end){
            tree[node] += diff;
            return;
        }

        int mid = (start+end)/2;
        update(node*2, start, mid, idx, diff);
        update(node*2+1, mid+1, end, idx, diff);
        tree[node] = tree[node*2] + tree[node*2+1];
    }

    void update(int idx, int diff){
        update(1, 0, n-1, idx, diff);
    }

    int sum_qry(int node, int start, int end, int left, int right){
        if (right < start || end < left) return 0;
        if (left <= start && end <= right) return tree[node];

        int mid = (start + end)/2;
        int l = sum_qry(node*2, start, mid, left, right);
        int r = sum_qry(node*2+1, mid+1, end, left, right);
        return l + r;
    }

    int sum_qry(int left, int right){
        return sum_qry(1, 0, n-1, left, right);
    }
};

int n;
pair<int, int> a[505050];
int new_a[505050];

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x; cin >> x;
        a[i] = {x, i};
    }

    sort(a, a+n);
    int range = 0;
    for (int i = 0; i < n; i++){
        if (i > 0 && a[i].first != a[i-1].first) range++;
        new_a[i] = range;
    }

    for (int i = 0; i < n; i++) a[i].first = new_a[i];
    sort(a, a+n, [](pair<int, int> x, pair<int, int> y){
        return x.second < y.second;
    });

    Seg seg(n);

    int ans = 0;
    for (int i = 0; i < n; i++){
        ans += seg.sum_qry(a[i].first+1, n-1);
        seg.update(a[i].first, 1);
    }

    cout << ans << '\n';
    
    return 0;
}