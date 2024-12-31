#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#define ll long long
#define int long long

using namespace std;

int n,m;
vector <pair<int, int>> line;

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> n >> m;
    for (int i = 0; i < n; i++){
        int x,y; cin >> x >> y;
        if (x > y) line.push_back({y,x});
    }

    sort(line.begin(), line.end());

    int INF = (int)1e9;
    int l = -INF, r = -INF;
    int ans = 0;

    for (int i = 0; i < line.size(); i++){
        int x = line[i].first;
        int y = line[i].second;

        if (x <= r) r = max(r, y);
        else{
            ans += r-l;
            l = x, r = y;
        }
    }
    ans += r - l;
    
    cout << ans*2 + m;
    return 0;
}

