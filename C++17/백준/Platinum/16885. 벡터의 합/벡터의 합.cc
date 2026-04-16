#include <bits/stdc++.h>
#define ll long long
#define ld long double
//#define int long long
const int inf = 1e9;

using namespace std;

struct Point{
    int x,y;
    int idx;
    int typ;

    Point(){};
    Point(int x, int y, int idx, int typ): x(x), y(y), idx(idx), typ(typ){}
};

int n;
array<int, 5> ans;
Point point[101010];

int ret_typ(int x, int y){
    if (x >= 0 && y >= 0) return 1;
    else if (x < 0 && y >= 0) return 2;
    else if (x >= 0 && y < 0) return 3;
    else return 4;
}

int get_dist_sq(Point a, Point b){
    return (a.x - b.x)*(a.x - b.x) + (a.y - b.y)*(a.y - b.y);
}

int go(int l, int r){
    if (l == r) return inf;
    int d = inf;
    int m = (l+r)/2;

    
    d = min(d, go(l, m));
    d = min(d, go(m+1, r));

    vector<Point> val;
    for (int i = l; i <= r; i++){
        if (pow(abs(point[m].x - point[i].x), 2) < d) val.push_back(point[i]);
    }

    sort(val.begin(), val.end(), [](Point a, Point b){
        return a.y < b.y;
    });

    for (int i = 0; i < val.size(); i++){
        for (int j = i+1; j < val.size(); j++){
            int gd = get_dist_sq(val[i], val[j]);
            if (pow(abs(val[i].y - val[j].y), 2) < d) {
                d = min(d, gd);
                if (d < ans[0]){
                    ans = {d, val[i].idx, val[i].typ, val[j].idx, val[j].typ};
                }
            }
            else break;
        }
    }

    return d;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++){
        int x,y; cin >> x >> y;
        point[i] = Point(abs(x),abs(y),i+1, ret_typ(x,y));
    }

    sort(point, point+n, [](Point a, Point b){
        return a.x < b.x;
    });

    ans[0] = inf;

    go(0, n-1);
 
    int typ = -1;
    if (ans[4] == 1) typ = 4;
    else if (ans[4] == 4) typ = 1;
    else if (ans[4] == 2) typ = 3;
    else typ = 2;

    cout << ans[1] << ' ' << ans[2] << ' ' << ans[3] << ' ' << typ << '\n';
    
    return 0;
}