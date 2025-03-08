#include <bits/stdc++.h>
// #define ll long long
// #define int long long
const int inf = 1e9;

using namespace std;

int n,k;
int tree[404040];

void update(int node, int start, int end, int idx, int val){
    if (start <= idx && idx <= end){
        tree[node] += val;
        if (start != end){
            int mid = (start+end)/2;
            update(node*2, start, mid, idx, val);
            update(node*2+1, mid+1, end, idx, val);
        }
    }
}

int kth(int node, int start, int end, int k){
    if (start == end) return start;

    int mid = (start+end)/2;
    if (tree[node*2] >= k) return kth(node*2, start, mid, k);
    else return kth(node*2+1, mid+1, end, k - tree[node*2]);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> k;
    
    for (int i = 1; i <= n; i++) update(1, 0, 100000, i, 1);

    cout << '<';
    int now = k-1;
    for (int i = n; i >= 1; i--){
        now %= i;
        int Kth = kth(1, 0, 100000, now+1);
        if (i != 1) cout << Kth << ", ";
        else cout << Kth << '>';
        update(1, 0, 100000, Kth, -1);
        now += k-1;
    }


    return 0;
}