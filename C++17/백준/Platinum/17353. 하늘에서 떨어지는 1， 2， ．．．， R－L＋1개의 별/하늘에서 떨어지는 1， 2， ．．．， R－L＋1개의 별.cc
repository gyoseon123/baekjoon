#include <bits/stdc++.h>
// #define ll long long
#define int long long
const int inf = 1e9;

using namespace std;

int n,q;
int base;
int a[1010101];
int b[1010101];
int tree[4040404];
int lazy[4040404];

void prop(int node, int start, int end){
    tree[node] += (end - start + 1) * lazy[node];
    if (start != end){
        lazy[node*2] += lazy[node];
        lazy[node*2+1] += lazy[node];
    }
    lazy[node] = 0;
    return;
}

void update(int node, int start, int end, int left, int right, int val){
    prop(node, start, end);
    if (right < start || end < left) return;
    if (left <= start && end <= right){
        lazy[node] += val;
        prop(node, start, end);
        return;
    }
    int mid = (start+end)/2;
    update(node*2, start, mid, left, right, val);
    update(node*2+1, mid+1, end, left, right, val);

    tree[node] = tree[node*2] + tree[node*2+1];
    return;
}

int qry(int node, int start, int end, int left, int right){
    prop(node, start, end);
    if (right < start || end < left) return 0;
    if (left <= start && end <= right) return tree[node];

    int mid = (start+end)/2;
    return qry(node*2, start, mid, left, right) + qry(node*2+1, mid+1, end, left, right);
}


signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    base = a[0];

    for (int i = 1; i < n; i++) {
        b[i] = a[i] - a[i-1];
        update(1, 0, n-1, i, i, b[i]);
    }

    cin >> q;
    for (int i = 0; i < q; i++){
        int op; cin >> op;
        if (op == 1){
            int l,r; cin >> l >> r;
            update(1, 0, n-1, l-1, r-1, 1);
            update(1, 0, n-1, r, r, -(r - l + 1));
        } else {
            int x; cin >> x;
            cout << qry(1, 0, n-1, 0, x-1) + base << '\n';
        }
    }
    
    return 0;
}