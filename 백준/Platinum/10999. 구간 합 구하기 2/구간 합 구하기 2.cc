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
#define MAX 1000000
using namespace std;

int n,m,k;
int arr[MAX];
int tree[MAX*4];
int lazy[MAX*4];

int prop(int node, int start, int end){
    tree[node] += (end - start + 1)*lazy[node];
    if (start != end) lazy[node*2] += lazy[node];
    if (start != end) lazy[node*2+1] += lazy[node];
    lazy[node] = 0;
    return 0;
}

int init(int node, int start, int end){
    if (start == end) return tree[node] = arr[start];
    int mid = (start+end)/2;
    return tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end);
}

int sum_query(int node, int start, int end, int left, int right){
    prop(node, start, end);
    if (left <= start && end <= right) return tree[node];
    if (right < start || end < left) return 0;
    int mid = (start+end)/2;
    return sum_query(node*2, start, mid, left, right) + sum_query(node*2+1, mid+1, end, left, right);
}

int update_query(int node, int start, int end, int left, int right, int diff){
    prop(node, start, end);
    if (left <= start && end <= right){
        // tree[node] += diff;
        lazy[node] += diff;
        prop(node, start, end);
        return 0;
    }
    if (right < start || end < left) return 0;
    
    int mid = (start+end)/2;
    update_query(node*2, start, mid, left, right, diff);
    update_query(node*2+1, mid+1, end, left, right, diff);
    
    tree[node] = tree[node*2] + tree[node*2+1];
    return 0;
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m >> k;
    for (int i = 0; i < n; i++) cin >> arr[i];
    init(1, 0, n-1);
    // for (int i = 0; i < 20; i++) cout << tree[i] << ' ';
    // cout << '\n';
    for (int i = 0; i < m+k; i++){
        int a; cin >> a;
        if (a == 1){
            int b,c,d; cin >> b >> c >> d;
            if (b > c) swap(b,c);
            update_query(1, 0, n-1, b-1, c-1, d);
            // for (int i = 0; i < 20; i++) cout << lazy[i] << ' ';
            // cout << '\n';
        } else {
            int b,c; cin >> b >> c;
            if (b > c) swap(b,c);
            cout << sum_query(1, 0, n-1, b-1, c-1) << '\n';
            // for (int i = 0; i < 20; i++) cout << tree[i] << ' ';
            // cout << '\n';
        }
    }

    return 0;
}