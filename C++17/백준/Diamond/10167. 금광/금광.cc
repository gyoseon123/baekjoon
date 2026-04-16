#include <bits/stdc++.h>
#define ll long long
// #define int long long
const int inf = 1e9;

using namespace std;
typedef array<ll, 3> arr;

struct Node {
    ll lmax;
    ll rmax;
    ll allmax;
    ll psum;

    Node(){}

    Node(ll v){
        lmax = rmax = allmax = psum = v;
    }
};

int n;
int range, newX[3030], newY[3030];
vector<arr> point;
vector<pair<int, int>> Ypoint[3030];
Node tree[12121];

void update(int node, int start, int end, int idx, int diff){
    if (idx < start || end < idx) return;
    if (start == end){
        tree[node].psum += diff;
        tree[node].allmax += diff;
        tree[node].lmax += diff;
        tree[node].rmax += diff;
        return;
    }

    int mid = (start+end)/2;
    update(node*2, start, mid, idx, diff);
    update(node*2+1, mid+1, end, idx, diff);
    Node Lnode = tree[node*2];
    Node Rnode = tree[node*2+1];

    tree[node].psum = Lnode.psum + Rnode.psum;
    tree[node].lmax = max(Lnode.lmax, Lnode.psum + Rnode.lmax);
    tree[node].rmax = max(Rnode.rmax, Rnode.psum + Lnode.rmax);
    tree[node].allmax = max(Lnode.rmax + Rnode.lmax, max(Lnode.allmax, Rnode.allmax));
    return;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++){
        ll x,y,w; cin >> x >> y >> w;
        point.push_back({x,y,w});
    }

    sort(point.begin(), point.end(), [](arr a, arr b){
        return a[0] < b[0];
    });

    range = 0;
    for (int i = 0; i < n; i++){
        if (i > 0 && point[i-1][0] != point[i][0]) range++;
        newX[i] = range;
    }
    
    for (int i = 0; i < n; i++) point[i][0] = newX[i];
    
    sort(point.begin(), point.end(), [](arr a, arr b){
        return a[1] < b[1];
    });

    range = 0;
    for (int i = 0; i < n; i++){
        if (i > 0 && point[i-1][1] != point[i][1]) range++;
        newY[i] = range;
    }

    for (int i = 0; i < n; i++) {
        point[i][1] = newY[i];
        Ypoint[newY[i]].push_back({point[i][0], point[i][2]});
    }

    ll ans = 0;

    for (int h1 = 0; h1 < 3030; h1++){
        for (int i = 0; i < 12121; i++){
            tree[i] = Node(0);
        }

        for (int h2 = h1; h2 < 3030; h2++){
            for (auto [x, w] : Ypoint[h2]){
                update(1, 0, 3030, x, w);
            }
            ans = max(ans, tree[1].allmax);
        }
    }

    cout << ans << '\n';
    
    return 0;
}