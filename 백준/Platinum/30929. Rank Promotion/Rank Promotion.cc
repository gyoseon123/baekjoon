#include <bits/stdc++.h>
// #define ll long long
#define int long long
const int inf = 1e18;

using namespace std;

int n,c,p,q;
string s;
int tree[2020202];
int y_psum[505050];

void update(int node, int start, int end, int idx, int val){
    if (idx < start || end < idx) return;
    if (start == end){
        tree[node] = val;
        return;
    }
    
    int mid = (start+end)/2;
    update(node*2, start, mid, idx, val);
    update(node*2+1, mid+1, end, idx, val);
    tree[node] = min(tree[node*2], tree[node*2+1]);
}

int min_qry(int node, int start, int end, int left, int right){
    if (right < start || end < left) return inf;
    if (left <= start && end <= right) return tree[node];

    int mid = (start+end)/2;
    int l = min_qry(node*2, start, mid, left, right);
    int r = min_qry(node*2+1, mid+1, end, left, right);
    return min(l, r);
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> c >> p >> q;
    cin >> s;
    s = "!" + s;

    for (int i = 1; i <= n; i++){
        y_psum[i] = y_psum[i-1] + (s[i] == 'Y');
        update(1, 0, n, i, y_psum[i-1]*q - p*i);
    }

    int last = 1;
    int ans = 0;
    for (int i = 1; i <= n; i++){
        int now_val = y_psum[i]*q - p*i - p;
        if (i - c + 1 < last) continue;
        int mn_val = min_qry(1, 0, n, last, i - c + 1);
        if (mn_val <= now_val){
            last = i+1;
            ans++;
        }
    }

    cout << ans << "\n";
    
    return 0;
}