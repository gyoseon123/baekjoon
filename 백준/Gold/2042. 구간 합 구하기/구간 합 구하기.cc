#include <bits/stdc++.h>
// #define ll long long
#define int long long
const int inf = 1e9;

using namespace std;

int tree[4040404];
int a[1010101];
int n,m,k;

int init(int node, int start, int end){
    if (start == end) return tree[node] = a[start];

    int mid = (start+end)/2;
    return tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end);
}

void update(int node, int start, int end, int idx, int val){
    if (idx < start || end < idx) return;
    if (start == end){
        tree[node] = a[idx] = val;
        return;
    }

    int mid = (start+end)/2;
    update(node*2, start, mid, idx, val);
    update(node*2+1, mid+1, end, idx, val);
    tree[node] = tree[node*2] + tree[node*2+1];
}

int qry(int node, int start, int end, int left, int right){
    if (right < start || end < left) return 0;
    if (left <= start && end <= right) return tree[node];

    int mid = (start+end)/2;

    return qry(node*2, start, mid, left, right) + qry(node*2+1, mid+1, end, left, right);
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m >> k;
    for (int i = 0; i < n; i++) cin >> a[i];
    init(1, 0, n-1);

    for (int i = 0; i < m+k; i++){
        int a,b,c; cin >> a >> b >> c;
        if (a == 1){
            update(1, 0, n-1, b-1, c);
        } else {
            cout << qry(1, 0, n-1, b-1, c-1) << '\n';
        }
    }
    
    return 0;
}