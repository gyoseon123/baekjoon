#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
// #define ll long long
#define int long long

using namespace std;

int n;
int tree[2000000*4];

int find_query(int node, int start, int end, int k){
    if (start == end) return start;
    int mid = (start+end)/2;
    if (k <= tree[node*2]) return find_query(node*2, start, mid, k);
    else return find_query(node*2+1, mid+1, end, k - tree[node*2]);
}

int update(int node, int start, int end, int idx, int diff){
    if (start <= idx && idx <= end){
        tree[node] += diff;
        if (start != end){
            int mid = (start+end)/2;
            update(node*2, start, mid, idx, diff);
            update(node*2+1, mid+1, end, idx, diff);
        }
    }
    return 0;
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++){
        int a,b; cin >> a >> b;
        if (a == 1){
            update(1, 0, 2000001, b, 1);
        } else {
            int ans = find_query(1, 0, 2000001, b);
            cout << ans << '\n';
            update(1, 0, 2000001, ans, -1);
        }
    }
    
    return 0;
}