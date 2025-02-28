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
// #define int long long
#define MAX 100000
using namespace std;

int n,m;
int s[MAX+1];
int e[MAX+1];
int tree[MAX*4];
int lazy[MAX*4];
vector <int> graph[100001];
int cnt = 0;

int prop(int node, int start, int end){
    tree[node] += lazy[node];
    if (start != end) lazy[node*2] += lazy[node];
    if (start != end) lazy[node*2+1] += lazy[node];
    lazy[node] = 0;
    return 0;
}

int update(int node, int start, int end, int left, int right, int diff){
    prop(node, start, end);
    if (left <= start && end <= right){
        lazy[node] += diff;
        prop(node, start, end);
        return 0;
    }
    if (right < start || end < left) return 0;
    
    int mid = (start+end)/2;
    update(node*2, start, mid, left, right, diff);
    update(node*2+1, mid+1, end, left, right, diff);
    tree[node] = tree[node*2] + tree[node*2+1];
    return 0;
}

int query(int node, int start, int end, int idx){
    prop(node, start, end);
    if (idx < start || end < idx) return 0;
    if (start == end){
        cout << tree[node] << '\n';
        return 0;
    }
    int mid = (start+end)/2;
    query(node*2, start, mid, idx);
    query(node*2+1, mid+1, end, idx);
    return 0;
}

void dfs(int now){
    s[now] = cnt++;
    for (auto next : graph[now]) dfs(next);
    e[now] = cnt-1;
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;
    for (int i = 1; i <= n; i++){
        int x; cin >> x;
        if (x != -1) graph[x].push_back(i);
    }
    
    dfs(1);

    for (int i = 0; i < m; i++){
        int q; cin >> q;
        if (q == 1){
            int a,b; cin >> a >> b;
            update(1, 0, n-1, s[a], e[a], b);
        } else {
            int a; cin >> a;
            query(1, 0, n-1, s[a]);
        }
    }


    return 0;
}