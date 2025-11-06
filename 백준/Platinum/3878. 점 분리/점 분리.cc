#include <bits/stdc++.h>
#define ll long long
//#define int long long
const int inf = 1e9;

using namespace std;


#define ld long double
const ld eps = 1e-12;
bool is_equal(ld a, ld b){return abs(a - b) < eps;}
struct Point{
    ld x,y;
    Point(){}
    Point(ld x, ld y){this->x = x, this->y = y;}
    bool operator<(const Point &other) const {
        if (is_equal(x, other.x)) return y < other.y;
        return x < other.x;
    }
    bool operator<=(const Point &other) const {
        if (is_equal(x, other.x)) return y < other.y || is_equal(y, other.y);
        return x < other.x || is_equal(x, other.x);
    }
    bool operator==(const Point &other) const {
        return is_equal(x, other.x) && is_equal(y, other.y);
    }
    Point operator+(const Point &other) const {
        return Point{x + other.x, y + other.y};
    }
    Point operator-(const Point &other) const {
        return Point{x - other.x, y - other.y};
    }
    Point operator*(ld t) const {
        return Point{x * t, y * t};
    }
};
struct Line{
    Point s,t; // 두 점으로 선을 표현, HPI에선 s->t 방향의 왼쪽을 선의 반평면으로 취급
    Line(){}
    Line(Point s, Point t){this->s = s, this->t = t;}
};
ld cross(Point p1, Point p2, Point p3){return (p2.x - p1.x)*(p3.y - p1.y) - (p3.x - p1.x)*(p2.y - p1.y);}
bool is_ccw(Point p1, Point p2, Point p3){return (p2.x - p1.x)*(p3.y - p1.y) - (p3.x - p1.x)*(p2.y - p1.y) > 0;}
bool is_cw(Point p1, Point p2, Point p3){return (p2.x - p1.x)*(p3.y - p1.y) - (p3.x - p1.x)*(p2.y - p1.y) < 0;}
ld point_dist(Point &a, Point &b){
    ld dx = (b.x - a.x);
    ld dy = (b.y - a.y);
    return sqrtl(dx*dx + dy*dy);
}
bool line_intersect(Line l1, Line l2, Point& p){ // 교점 없으면 false, 있으면 true리턴 후 p에 교점 저장
    ld dx1 = l1.t.x - l1.s.x;
    ld dy1 = l1.t.y - l1.s.y;
    ld dx2 = l2.t.x - l2.s.x;
    ld dy2 = l2.t.y - l2.s.y;
    ld det = dx1 * (-dy2) - (-dx2) * dy1;
    if (is_equal(det, 0)) return false;

    ld s = ((l2.s.x - l1.s.x) * (-dy2) + (l2.s.y - l1.s.y) * dx2) / det;
	p.x = l1.s.x + dx1 * s;
	p.y = l1.s.y + dy1 * s;
    return true;
}
ld find_area(vector<Point> points){ // 다각형 넓이
    vector<ld> numX;
    vector<ld> numY;
    ld sumP = 0, sumM = 0;
    for (auto [x,y] : points){
        numX.push_back(x);
        numY.push_back(y);
    }
    if (!numX.empty()) numX.push_back(numX[0]);
    if (!numY.empty()) numY.push_back(numY[0]);

    int n = points.size();
    for (int i = 0; i < n; i++){
        sumP += (numX[i] * numY[i+1]);
        sumM += (numX[n - i] * numY[n - i - 1]);
    }

    return abs(sumP - sumM)/2;
}

vector<Point> convex_hull(vector<Point> points){
    sort(points.begin(), points.end());
    vector<Point> stk1;
    vector<Point> stk2;
    for (auto p : points){
        while (stk1.size() >= 2){
            if (cross(stk1[stk1.size()-2], stk1[stk1.size()-1], p) >= 0) stk1.pop_back();
            else break;
        }

        while (stk2.size() >= 2){
            if (cross(stk2[stk2.size()-2], stk2[stk2.size()-1], p) <= 0) stk2.pop_back();
            else break;
        }

        stk1.push_back(p);
        stk2.push_back(p);
    }

    vector<Point> ret;
    for (int i = 0; i < stk1.size(); i++) ret.push_back(stk1[i]);
    for (int i = stk2.size()-2; i >= 1; i--) ret.push_back(stk2[i]);
    return ret;
}

int is_in(vector<Point> convex_hull, Point p){
    int cnt = 0;
    int s = convex_hull.size();
    for (int i = 0; i < s; i++){
        int dir = cross(convex_hull[i], convex_hull[(i+1)%s], p);
        if (dir < 0) cnt++;
        if (dir == 0){
            vector<Point> points = {convex_hull[i], convex_hull[(i+1)%s], p};
            sort(points.begin(), points.end());
            if (points[1] == p) cnt++;
        }
    }
    return cnt == s;
}

int is_cross(Point p1, Point p2, Point p3, Point p4){
    int dir1 = cross(p1, p2, p3)*cross(p1, p2, p4);
    int dir2 = cross(p3, p4, p1)*cross(p3, p4, p2);

    if (dir1 == 0 && dir2 == 0){
        if (p1 < p2) swap(p1, p2);
        if (p3 < p4) swap(p3, p4);

        return (p3 <= p2 && p1 <= p4) || (p2 <= p3 && p4 <= p1);
    }
    return dir1 <= 0 && dir2 <= 0;
}

void solve(){
    int n,m; cin >> n >> m;
    vector<Point> white;
    vector<Point> black;
    for (int i = 0; i < n; i++){
        int x,y; cin >> x >> y;
        white.push_back(Point(x,y));
    }
    for (int i = 0; i < m; i++){
        int x,y; cin >> x >> y;
        black.push_back(Point(x,y));
    }

    vector<Point> wch = convex_hull(white);
    vector<Point> bch = convex_hull(black);

    bool in_point = false;

    if (wch.size() >= 2){
        for (auto p : black){
            in_point |= is_in(wch, p);
        }
    }
    if (bch.size() >= 2){
        for (auto p : white){
            in_point |= is_in(bch, p);
        }
    }

    if (wch.size() == 2 && bch.size() == 2){
        if (is_cross(wch[0], wch[1], bch[0], bch[1])) cout << "NO" << '\n';
        else cout << "YES" << '\n';
    } else {
        if (in_point) cout << "NO" << '\n';
        else cout << "YES" << '\n';
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t; cin >> t;
    while (t--) solve();
    
    return 0;
}