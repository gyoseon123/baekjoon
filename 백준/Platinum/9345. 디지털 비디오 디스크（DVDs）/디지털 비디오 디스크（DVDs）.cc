#include <bits/stdc++.h>
#define ll long long
//#define int long long
const int inf = 1e9;

using namespace std;

int max_tree[404040];
int min_tree[404040];
int pos[101010];

void update(int node, int start, int end, int idx, int val, int tree[], int is_min){
    if (idx < start || end < idx) return;
    if (start == end){
        tree[node] = val;
        return;
    }

    int mid = (start+end)/2;
    update(node*2, start, mid, idx, val, tree, is_min);
    update(node*2+1, mid+1, end, idx, val, tree, is_min);
    if (is_min) tree[node] = min(tree[node*2], tree[node*2+1]);
    else tree[node] = max(tree[node*2], tree[node*2+1]);
}

int qry(int node, int start, int end, int left, int right, int tree[], int is_min){
    if (right < start || end < left) {
        if (is_min) return inf;
        else return -inf;
    }
    if (left <= start && end <= right) return tree[node];

    int mid = (start+end)/2;
    if (is_min) return min(qry(node*2, start, mid, left, right, tree, is_min), qry(node*2+1, mid+1, end, left, right, tree, is_min));
    else return max(qry(node*2, start, mid, left, right, tree, is_min), qry(node*2+1, mid+1, end, left, right, tree, is_min));
}

void solve(){
    int n,k; cin >> n >> k;
    for (int i = 0; i < 404040; i++){
        min_tree[i] = inf;
        max_tree[i] = -inf;
    }

    for (int i = 0; i < n; i++){
        pos[i] = i;
        update(1, 0, 101010, i, i, min_tree, 1);
        update(1, 0, 101010, i, i, max_tree, 0);
    }

    for (int i = 0; i < k; i++){
        int op; cin >> op;
        if (op == 0){
            int a,b; cin >> a >> b;
            update(1, 0, 101010, pos[a], b, min_tree, 1);
            update(1, 0, 101010, pos[b], a, min_tree, 1);
            update(1, 0, 101010, pos[a], b, max_tree, 0);
            update(1, 0, 101010, pos[b], a, max_tree, 0);
            swap(pos[a], pos[b]);
        } else {
            int a,b; cin >> a >> b;
            int mn = qry(1, 0, 101010, a, b, min_tree, 1);
            int mx = qry(1, 0, 101010, a, b, max_tree, 0);
            if (mn == a && mx == b) cout << "YES" << '\n';
            else cout << "NO" << '\n';
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t; cin >> t;
    while (t--) solve();
    
    return 0;
}