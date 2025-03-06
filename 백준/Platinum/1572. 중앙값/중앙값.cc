#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <stack>
#include <unordered_set>
#include <cmath>
// #define ll long long
#define int long long

using namespace std;

int n,k;
int arr[250000];
int tree[1000000];
int ans = 0;

int update(int node, int start, int end, int val, int diff){
    if (start <= val && val <= end){
        tree[node] += diff;
        if (start != end){
            int mid = (start+end)/2;
            update(node*2, start, mid, val, diff);
            update(node*2+1, mid+1, end, val, diff);
        }
    }
    return 0;
}

int find(int node, int start, int end, int k){
    if (start == end) return start;
    int mid = (start+end)/2;
    if (k <= tree[node*2]) return find(node*2, start, mid, k);
    else return find(node*2+1, mid+1, end, k - tree[node*2]);
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> k;
    for (int i = 0; i < n; i++) cin >> arr[i];

    for (int i = 0; i < k; i++) update(1, 0, 250000, arr[i], 1);
    ans += find(1, 0, 250000, (k+1)/2);
    for (int i = k; i < n; i++){
        update(1, 0, 250000, arr[i], 1);
        update(1, 0, 250000, arr[i-k], -1);
        ans += find(1, 0, 250000, (k+1)/2);
    }

    cout << ans;

    return 0;
}