#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <cstring>
// #define ll long long
#define int long long

using namespace std;

int n;
int tree[75000*4];
vector <pair<int, int>> point;

int sum_query(int node, int start, int end, int left, int right){
    if (left <= start && end <= right) return tree[node];
    if (right < start || end < left) return 0;
    int mid = (start+end)/2;
    return sum_query(node*2, start, mid, left, right) + sum_query(node*2+1, mid+1, end, left, right);
}

int update_query(int node, int start, int end, int idx){
    if (start <= idx && idx <= end){
        tree[node]++;
        if (start != end){
            int mid = (start+end)/2;
            update_query(node*2, start, mid, idx);
            update_query(node*2+1, mid+1, end, idx);
        }
    }
    return 0;
}

int solve(){
    memset(tree, 0, sizeof(tree));
    point.clear();

    cin >> n;
    for (int i = 0; i < n; i++){
        int x,y; cin >> x >> y;
        point.push_back({x,y});
    }

    sort(point.begin(), point.end(), [](pair<int, int> a, pair<int, int> b){
        return a.second < b.second;
    });

    int newY[75000];
    int range = 0;
    for (int i = 0; i < n; i++){
        if (i > 0 && point[i].second != point[i-1].second) range++;
        newY[i] = range;
    }

    for (int i = 0; i < n; i++) point[i].second = newY[i];

    sort(point.begin(), point.end(), [](pair<int, int> a, pair<int, int> b){
        if (a.first == b.first) return a.second > b.second;
        return a.first < b.first;
    });

    int ans = 0;
    for (int i = 0; i < n; i++){
        int y = point[i].second;
        ans += sum_query(1, 0, n-1, y, 75000*4);
        update_query(1, 0, n-1, y);
    }
    
    cout << ans << '\n';
    return 0;    
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    int t; cin >> t;
    for (int i = 0; i < t; i++) solve();
    
    return 0;
}