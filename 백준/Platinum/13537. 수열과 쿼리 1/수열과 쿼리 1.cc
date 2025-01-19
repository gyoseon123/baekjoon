#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <stack>
#include <unordered_set>
#include <cmath>
#include <map>
// #define ll long long
#define int long long

using namespace std;

int n,m;
vector<int> tree[404040];

void update(int node, int start, int end, int idx, int val){
    if (idx < start || end < idx) return;
    tree[node].push_back(val);
    if (start != end){
        int mid = (start+end)/2;
        update(node*2, start, mid, idx, val);
        update(node*2+1, mid+1, end, idx, val);
    }
    return;
}

int find_query(int node, int start, int end, int left, int right, int k){
    if (left <= start && end <= right) return tree[node].end() - upper_bound(tree[node].begin(), tree[node].end(), k);
    if (right < start || end < left) return 0;
    int mid = (start+end)/2;
    return find_query(node*2, start, mid, left, right, k) + find_query(node*2+1, mid+1, end, left, right, k);
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++){
        int x; cin >> x;
        update(1, 0, n-1, i, x);
    }

    for (int i = 0; i < 404040; i++){
        sort(tree[i].begin(), tree[i].end());
    }

    cin >> m; 
    for (int i = 0; i < m; i++){
        int a,b,c; cin >> a >> b >> c;
        cout << find_query(1, 0, n-1, a-1, b-1, c) << '\n';
    }


    return 0;
}