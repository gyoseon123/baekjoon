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

using namespace std;

int n;
vector <pair<int, int>> point;

bool check(int x1, int y1, int x2, int y2, int x3, int y3){
    int a = (x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2);
    int b = (x2 - x3)*(x2 - x3) + (y2 - y3)*(y2 - y3);
    int c = (x1 - x3)*(x1 - x3) + (y1 - y3)*(y1 - y3);

    return (a + b == c) || (b + c == a) || (c + a == b);
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++){
        int x,y; cin >> x >> y;
        point.push_back({x,y});
    }

    int ans = 0;
    for (int i = 0; i < n; i++){
        for (int j = i+1; j < n; j++){
            for (int k = j+1; k < n; k++){
                if (check(point[i].first, point[i].second, point[j].first, point[j].second, point[k].first, point[k].second)) ans++;
            }
        }
    }

    cout << ans;

    return 0;
}