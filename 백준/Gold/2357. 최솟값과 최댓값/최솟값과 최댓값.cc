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
#define INF 1000000000;
using namespace std;

int n,m;
int arr[100000];
int mintree[400000];
int maxtree[400000];

int init_min(int node, int start, int end){
    if (start == end) return mintree[node] = arr[start];
    int mid = (start+end)/2;
    return mintree[node] = min(init_min(node*2, start, mid), init_min(node*2+1, mid+1, end));
}

int init_max(int node, int start, int end){
    if (start == end) return maxtree[node] = arr[start];
    int mid = (start+end)/2;
    return maxtree[node] = max(init_max(node*2, start, mid), init_max(node*2+1, mid+1, end));
}

int minq(int node, int start, int end, int left, int right){
    if (left <= start && end <= right) return mintree[node];
    if (right < start || end < left) return INF;
    int mid = (start+end)/2;
    return min(minq(node*2, start, mid, left, right), minq(node*2+1, mid+1, end, left, right));
}

int maxq(int node, int start, int end, int left, int right){
    if (left <= start && end <= right) return maxtree[node];
    if (right < start || end < left) return -INF;
    int mid = (start+end)/2;
    return max(maxq(node*2, start, mid, left, right), maxq(node*2+1, mid+1, end, left, right));
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;
    for (int i = 0; i < n; i++) cin >> arr[i];
    init_min(1, 0, n-1);
    init_max(1, 0, n-1);

    for (int i = 0; i < m; i++){
        int a,b; cin >> a >> b;
        cout << minq(1, 0, n-1, a-1, b-1) << ' ' << maxq(1, 0, n-1, a-1, b-1) << '\n';
    }

    return 0;
}