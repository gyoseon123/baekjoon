#include <bits/stdc++.h>
#define ll long long
#define ld long double
//#define int long long
const int inf = 1e9;

using namespace std;

struct Point{
    int x,y;

    Point(){};
    Point(int x, int y): x(x), y(y){}
};

int n;
Point point[101010];

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
            if (pow(abs(val[i].y - val[j].y), 2) < d) d = min(d, gd);
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
        point[i] = Point(x,y);
    }

    sort(point, point+n, [](Point a, Point b){
        return a.x < b.x;
    });

    cout << go(0, n-1) << '\n';
    
    return 0;
}