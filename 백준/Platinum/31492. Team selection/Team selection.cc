#include <bits/stdc++.h>
// #define ll long long
#define int long long
const int inf = 1e9;

using namespace std;

int n;
int tree[12121212];

void init(int node, int start, int end){
    if (start == end){
        tree[node] = 1;
        return;
    }

    int mid = (start+end)/2;
    init(node*2, start, mid);
    init(node*2+1, mid+1, end);
    tree[node] = tree[node*2] + tree[node*2+1];
}

void update(int node, int start, int end, int idx, int diff){
    if (idx < start || end < idx) return;
    if (start == end){
        tree[node] += diff;
        return;
    }

    int mid = (start+end)/2;
    update(node*2, start, mid, idx, diff);
    update(node*2+1, mid+1, end, idx, diff);
    tree[node] = tree[node*2] + tree[node*2+1];
}

int kth(int node, int start, int end, int k){
    if (start == end) return start;
    
    int mid = (start+end)/2;
    if (k <= tree[node*2]) return kth(node*2, start, mid, k);
    else return kth(node*2+1, mid+1, end, k - tree[node*2]);
}


signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;
    init(1, 1, n);
    vector<int> a;
    vector<int> b;
    for (int i = 0; i < n/2; i++){
        int x; cin >> x;
        a.push_back(x);
    }
    for (int i = 0; i < n/2; i++){
        int x; cin >> x;
        b.push_back(x);
    }

    vector<int> a_ans;
    vector<int> b_ans;

    int k;
    for (int i = 0; i < n/2; i++){
        k = kth(1, 1, n, a[i]);
        a_ans.push_back(k);
        update(1, 1, n, k, -1);
        k = kth(1, 1, n , b[i]);
        b_ans.push_back(k);
        update(1, 1, n, k, -1);
    }

    for (auto x : a_ans) cout << x << ' ';
    cout << '\n';
    for (auto x : b_ans) cout << x << ' ';
    cout << '\n';
    
    return 0;
}