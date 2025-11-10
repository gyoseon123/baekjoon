#include <bits/stdc++.h>
// #define ll long long
#define int long long
const int inf = 1e9;

using namespace std;
typedef array<int, 3> arr;

int n;
vector<pair<int, int>> points[1010101];
vector<int> x_points;
int parent[101010];
int rnk[101010];

int find(int x){
    if (parent[x] != x) return parent[x] = find(parent[x]);
    return parent[x];
}

int dist(int x1, int y1, int x2, int y2){
    int dx = (x2 - x1);
    int dy = (y2 - y1);
    return (dx*dx + dy*dy);
}

void merge(int a, int b){
    a = find(a);
    b = find(b);

    if (a == b) return;

    if (rnk[a] < rnk[b]) swap(a,b);
    parent[b] = a;
    if (rnk[a] == rnk[b]) rnk[a]++;
}


signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++){
        int x,y; cin >> x >> y;
        points[x].push_back({y,i});
        x_points.push_back(x);
        parent[i] = i;
    }

    sort(x_points.begin(), x_points.end());
    x_points.erase(unique(x_points.begin(), x_points.end()), x_points.end());

    vector<arr> edges;
    for (int i = 0; i < x_points.size(); i++){
        int x = x_points[i];
        for (auto [y1, idx1] : points[x]){
            for (auto [y2, idx2] : points[x]){
                if (idx1 == idx2) continue;
                edges.push_back({dist(x, y1, x, y2), idx1, idx2});
            }
        }
        
        for (auto [y1, idx1] : points[x]){
            for (int j = i+1; j < min((int)x_points.size(), i+10); j++){
                for (auto [y2, idx2] : points[x_points[j]]){
                    edges.push_back({dist(x, y1, x_points[j], y2), idx1, idx2});
                }
            }
        }
    }

    sort(edges.begin(), edges.end());

    int ans = 0;
    for (auto [c, a, b] : edges){
        if (find(a) != find(b)){
            ans += c;
            merge(a,b);
        }
    }

    cout << ans << '\n';
    
    return 0;
}