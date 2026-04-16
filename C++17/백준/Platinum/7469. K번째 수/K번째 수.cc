#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <cstring>
// #define ll long long
// #define int long long

using namespace std;

int n,q;
vector<int> tree[404040];

void update(int node, int start, int end, int idx, int val){
    if (idx < start || end < idx) return;
    tree[node].push_back(val);
    if (start != end){
        int mid = (start+end)/2;
        update(node*2, start, mid, idx, val);
        update(node*2+1, mid+1, end, idx, val);
    }
}

int find_query(int node, int start, int end, int left, int right, int x){
    if (right < start || end < left) return 0;
    if (left <= start && end <= right) return upper_bound(tree[node].begin(), tree[node].end(), x) - tree[node].begin();
    int mid = (start+end)/2;
    return find_query(node*2, start, mid, left, right, x) + find_query(node*2+1, mid+1, end, left, right, x);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> n >> q;
    for (int i = 0; i < n; i++){
        int x; cin >> x;
        update(1, 0, n-1, i, x);
    }

    for (int i = 0; i < 404040; i++) sort(tree[i].begin(), tree[i].end());

    for (int i = 0; i < q; i++){
        int a,b,c; cin >> a >> b >> c;
        int left = -1e9-1;
        int right = 1e9+1;
        while (left + 1 < right){
            int mid = (left+right)/2;
            int cnt = find_query(1, 0, n-1, a-1, b-1, mid);

            if (cnt >= c) right = mid;
            else left = mid;
        }

        cout << right << '\n';
    }
    
    return 0;
}