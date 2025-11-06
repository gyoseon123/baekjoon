#include <bits/stdc++.h>
#define ll long long
//#define int long long
const int inf = 1e9;

using namespace std;


#define sz(x) ((int)x.size())
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
Point find_point(Point p1, Point p2, Point p3){
    return Point(p3.x - p2.x + p1.x, p3.y - p2.y + p1.y);
}
ld find_area(vector<Point> &points){ // 다각형 넓이
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

vector<Point> convex_hull(vector<Point> &points){
    sort(points.begin(), points.end());
    vector<Point> stk1;
    vector<Point> stk2;
    for (auto p : points){
        while (sz(stk1) >= 2){
            if (cross(stk1[sz(stk1)-2], stk1[sz(stk1)-1], p) >= 0) stk1.pop_back();
            else break;
        }

        while (sz(stk2) >= 2){
            if (cross(stk2[sz(stk2)-2], stk2[sz(stk2)-1], p) <= 0) stk2.pop_back();
            else break;
        }

        stk1.push_back(p);
        stk2.push_back(p);
    }

    vector<Point> ret;
    for (int i = 0; i < sz(stk1); i++) ret.push_back(stk1[i]);
    for (int i = sz(stk2)-2; i >= 1; i--) ret.push_back(stk2[i]);
    return ret;
}

int is_in(vector<Point> &convex_hull, Point p){
    int cnt = 0;
    int s = sz(convex_hull);
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

ld find_max_dist(vector<Point> &points){
    int n = points.size();
    int r = 0;
    ld ret = 0;

    for (int i = 0; i < n; i++){
        while (r < 2*n && is_ccw(points[i], points[(i+1)%n], find_point(points[(i+1)%n], points[r%n], points[(r+1)%n]))){
            ret = max(ret, point_dist(points[i], points[r%n]));
            r += 1;
        }
        ret = max(ret, point_dist(points[i], points[r%n]));
    }
    return ret;
}


Line inner_line(Line l, ld itv){
    ld dx = l.t.x - l.s.x;
    ld dy = l.t.y - l.s.y;
    ld x_itv = ((-dy) / sqrtl(dx * dx + dy * dy)) * itv;
    ld y_itv = (dx / sqrtl(dx * dx + dy * dy)) * itv;
    Line ret;
    ret.s.x = l.s.x + x_itv;
    ret.s.y = l.s.y + y_itv;
    ret.t.x = l.t.x + x_itv;
    ret.t.y = l.t.y + y_itv;
    return ret;
}

bool is_hide(Line a, Line b, Line c){
    Point p;
    if (!line_intersect(a, b, p)) return 0;
    ld crs = cross(c.s, c.t, p);
    return (crs < 0);
}

vector<Point> HPI(vector<Line> lines){
    auto line_div = [&](Line l){ // line을 0~180 / 180~360 구간으로 나눔
        if (is_equal(l.s.y, l.t.y)) return l.s.x > l.t.x;
        return l.s.y > l.t.y;
    };

    sort(lines.begin(), lines.end(), [&](Line l1, Line l2){
        if (line_div(l1) != line_div(l2)) return line_div(l1) < line_div(l2);
        ld crs = (l1.t.x - l1.s.x) * (l2.t.y - l2.s.y) - (l1.t.y - l1.s.y) * (l2.t.x - l2.s.x);
        if (!is_equal(crs, 0)) return crs > 0;
        return is_ccw(l1.s, l1.t, l2.s);
    });

    vector<Line> unique_lines;
    if (!lines.empty()) {
        unique_lines.push_back(lines[0]);
        for (int i = 1; i < lines.size(); i++) {
            ld crs = (unique_lines.back().t.x - unique_lines.back().s.x) * (lines[i].t.y - lines[i].s.y) -
                     (unique_lines.back().t.y - unique_lines.back().s.y) * (lines[i].t.x - lines[i].s.x);
            if (is_equal(crs, 0)) {
                unique_lines.back() = lines[i];
            } else {
                unique_lines.push_back(lines[i]);
            }
        }
    }

    lines = vector<Line>(unique_lines);

    deque<Line> dq;
    for (int i = 0; i < lines.size(); i++){
        while (sz(dq) >= 2 && is_hide(dq[sz(dq)-2], dq[sz(dq)-1], lines[i])) dq.pop_back();
        while (sz(dq) >= 2 && is_hide(dq[0], dq[1], lines[i])) dq.pop_front();
        if (sz(dq) < 2 || !is_hide(dq[sz(dq)-1], lines[i], dq[0])) dq.push_back(lines[i]);
    }
    
    while (sz(dq) >= 2 && is_hide(dq[sz(dq)-2], dq[sz(dq)-1], dq[0])) dq.pop_back();
    while (sz(dq) >= 2 && is_hide(dq[sz(dq)-1], dq[0], dq[1])) dq.pop_front();


    vector<Point> ret;
    int n = sz(dq);
    if (n >= 3){
        for (int i = 0; i < n; i++){
            int j = (i+1)%n;
            Point p;
            if (!line_intersect(dq[i], dq[j], p)) continue;
            ret.push_back(p);
        }
    }

    return ret;
}
bool check(ld radi, const vector<Line>& lines){
    vector<Line> new_lines;
    for (int i = 0; i < sz(lines); i++){
        new_lines.push_back(inner_line(lines[i], radi));
    }
    vector<Point> hpi = HPI(new_lines);

    ld max_d = find_max_dist(hpi);

    if (max_d >= radi*2) return true;
    return false;
}

void solve(int n){
    vector<Point> p;
    for (int i = 0; i < n; i++){
        int x,y; cin >> x >> y;
        p.push_back(Point(x,y));
    }

    vector<Line> lines;
    for (int i = 0; i < n; i++){
        Point p1 = p[i%n];
        Point p2 = p[(i+1)%n];
        lines.push_back(Line(p1, p2));
    }

    ld left = 0;
    ld right = 1e9;
    for (int i = 0; i < 50; i++){
        ld mid = (left+right)/2;
        if (check(mid, lines)) left = mid;
        else right = mid;
    }

    cout << fixed;
    cout.precision(3);
    cout << left << '\n';
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n; cin >> n;
    solve(n);
    
    return 0;
}