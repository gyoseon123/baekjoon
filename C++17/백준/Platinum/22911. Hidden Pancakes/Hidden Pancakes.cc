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
const int MOD = 1e9 + 7;

using namespace std;

int N,M,t;
int arr[101010];
int tree[404040];
int fac[101010];

int comp(int x, int y){
    if (x == -1) return y;
    if (y == -1) return x;
    if (arr[x] == arr[y]) return (x < y) ? y : x;
    return (arr[x] < arr[y]) ? x : y;
}

int update(int node, int start, int end, int idx){
    if (idx < start || end < idx) return tree[node];
    if (start == end) return tree[node] = idx;
    int mid = (start+end)/2;
    return tree[node] = comp(update(node*2, start, mid, idx), update(node*2+1, mid+1, end, idx));
}

int find_query(int node, int start, int end, int left, int right){
    if (left <= start && end <= right) return tree[node];
    if (right < start || end < left) return -1;
    int mid = (start+end)/2;
    return comp(find_query(node*2, start, mid, left, right), find_query(node*2+1, mid+1, end, left, right));
}


int Pow(int x, int cnt){
    if (cnt == 1) return x;

    int t = Pow(x, cnt/2);
    if (cnt&1) return ((t*t)%MOD*x)%MOD;
    else return (t*t)%MOD;
}

int C(int n, int k){
    return (fac[n]*Pow((fac[n-k]*fac[k])%MOD, MOD-2)%MOD);
}

int f(int l, int r){
    if (r < l) return 1;

    int mid = find_query(1, 0, N-1, l, r);
    int left = find_query(1, 0, N-1, l, mid-1);
    int right = find_query(1, 0, N-1, mid+1, r);

    if (l < mid && arr[left] != arr[mid]) return 0;
    if (mid < r && arr[right] != arr[mid]+1) return 0;

    return C(r-l, mid - l) * f(l, mid-1) % MOD * f(mid+1, r) % MOD;
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    fac[0] = 1;
    for (int i = 1; i <= 100000; i++) fac[i] = (fac[i-1]*i)%MOD;

    cin >> t;
    for (int test = 1; test <= t; test++){
        cin >> N;
        for (int i = 0; i < N; i++){
            cin >> arr[i];
            update(1, 0, N-1, i);
        }

        cout << "Case #" << test << ": " << f(0, N-1) << '\n';
    }

    return 0;
}