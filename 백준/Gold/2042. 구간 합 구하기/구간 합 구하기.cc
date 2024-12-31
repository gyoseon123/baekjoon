#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#define int long long

using namespace std;

int n,m,k;
int arr[1000000];
int tree[4000000];

int init(int node, int start, int end){
    if (start == end) return tree[node] = arr[start];
    int mid = (start+end)/2;
    return tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end);
}

int sum_query(int node, int start, int end, int left, int right){
    if (left <= start && end <= right) return tree[node];
    if (right < start || end < left) return 0;
    int mid = (start+end)/2;
    return sum_query(node*2, start, mid, left, right) + sum_query(node*2+1, mid+1, end, left, right);
}

int update_query(int node, int start, int end, int idx, int diff){
    if (start <= idx && idx <= end){
        tree[node] += diff;
        if (start != end){
            int mid = (start+end)/2;
            update_query(node*2, start, mid, idx, diff);
            update_query(node*2+1, mid+1, end, idx, diff);
        }
    }
    return 0;
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> n >> m >> k;
    for (int i = 0; i < n; i++) cin >> arr[i];
    init(1, 0, n-1);

    for (int i = 0; i < m+k; i++){
        int a,b,c; cin >> a >> b >> c;
        if (a == 1){
            int diff = c - arr[b-1];
            arr[b-1] = c;
            update_query(1, 0, n-1, b-1, diff);
        } else {
            cout << sum_query(1, 0, n-1, b-1, c-1) << '\n';
        }
    }
    
    return 0;
}