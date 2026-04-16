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
bool is_ccw(Point p1, Point p2, Point p3){return (p2.x - p1.x)*(p3.y - p1.y) - (p3.x - p1.x)*(p2.y - p1.y) >= 0;}
bool is_cw(Point p1, Point p2, Point p3){return (p2.x - p1.x)*(p3.y - p1.y) - (p3.x - p1.x)*(p2.y - p1.y) <= 0;}
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

ld point_to_line_dist(Point p, Line line){
    Point v = line.t - line.s;
    Line l = Line(p, Point(p.x - v.y, p.y + v.x));
    Point int_p;
    line_intersect(line, l, int_p);
    return point_dist(int_p, p);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n; cin >> n;
    vector<Point> points;
    for (int i = 0; i < n; i++){
        ld x,y; cin >> x >> y;
        points.push_back(Point(x,y));
    }

    ld ans = 0;
    for (int i = 0; i < n; i++){
        Point prepre = points[(i-2+n)%n];
        Point pre = points[(i-1+n)%n];
        Point now = points[i];
        Point suc = points[(i+1)%n];
        Point sucsuc = points[(i+2)%n];
        Line l1 = Line(prepre, pre);
        Line l2 = Line(sucsuc, suc);
        Point p;
        bool ret = line_intersect(l1, l2, p);
        
        Point mid = (pre + suc)*(1.0/2.0);
        Point v = mid - pre;
        ld r = point_dist(mid, pre);
        Point basis = Point(v.y, -v.x)*(1.0 / sqrtl(v.x*v.x + v.y*v.y));
        Point circle_mid = mid + basis * r;

        bool pre_out = false;
        bool suc_out = false;

        Point v1 = mid - pre;
        Point v2 = prepre - pre;
        if (v1.x * v2.x + v1.y * v2.y > 0 || is_equal(v1.x * v2.x + v1.y * v2.y, 0)) pre_out = true;
        v1 = mid - suc;
        v2 = sucsuc - suc;
        if (v1.x * v2.x + v1.y * v2.y > 0 || is_equal(v1.x * v2.x + v1.y * v2.y, 0)) suc_out = true;
        
        if (!pre_out && !suc_out){
            // cout << i << ' ' << 1111 << '\n';
            Line l1 = Line(prepre, pre);
            Line l2 = Line(sucsuc, suc);
            if (is_ccw(prepre, pre, circle_mid) && is_cw(sucsuc, suc, circle_mid)){
                ld ori = point_dist(pre, now) + point_dist(now, suc);
                ld d = point_dist(pre, circle_mid) + point_dist(circle_mid, suc);
                ans = max(ans, d - ori);
            }
            
            if (point_dist(mid, p) <= r){
                ld d = point_dist(pre, p) + point_dist(p, suc);
                ld ori = point_dist(pre, now) + point_dist(now, suc);
                ans = max(ans, d - ori);
            } else {
                ld r = point_dist(mid, pre);
                ld d = point_to_line_dist(mid, l1);
                ld x = 2*sqrtl(r*r - d*d);
                ld y = sqrtl((4*r*r) - x*x);
                ld ori = point_dist(pre, now) + point_dist(now, suc);
                ld dd = x + y;
                ans = max(ans, dd - ori);
                
                r = point_dist(mid, suc);
                d = point_to_line_dist(mid, l2);
                x = 2*sqrtl(r*r - d*d);
                y = sqrtl((4*r*r) - x*x);
                ori = point_dist(pre, now) + point_dist(now, suc);
                dd = x + y;
                ans = max(ans, dd - ori);
            }
        } else if (pre_out && !suc_out){
            // cout << i << ' ' << 2222 << '\n';
            
            Point v = pre - prepre;
            Line l = Line(pre, Point(pre.x - v.y, pre.y+v.x));
            Point int_p;
            line_intersect(l, Line(sucsuc, suc), int_p);

            if (point_dist(mid, int_p) <= r){
                ld r = point_dist(mid, pre);
                ld d = point_to_line_dist(mid, Line(sucsuc, suc));
                ld x = 2*sqrtl(r*r - d*d);
                ld y = sqrtl((4*r*r) - x*x);
                ld ori = point_dist(pre, now) + point_dist(now, suc);
                ld dd = x + y;
                ans = max(ans, dd - ori);
                r = point_dist(mid, suc);
                d = point_to_line_dist(mid, l2);
                x = 2*sqrtl(r*r - d*d);
                y = sqrtl((4*r*r) - x*x);
                ori = point_dist(pre, now) + point_dist(now, suc);
                dd = x + y;
                ans = max(ans, dd - ori);
            } else {
                ld r = point_dist(mid, pre);
                ld d = point_to_line_dist(mid, l);
                ld x = 2*sqrtl(r*r - d*d);
                ld y = sqrtl((4*r*r) - x*x);
                ld ori = point_dist(pre, now) + point_dist(now, suc);
                ld dd = x + y;
                ans = max(ans, dd - ori);
            }

            if (is_cw(l.s, l.t, circle_mid) && is_cw(sucsuc, suc, circle_mid)){
                ld ori = point_dist(pre, now) + point_dist(now, suc);
                ld d = point_dist(pre, circle_mid) + point_dist(circle_mid, suc);
                ans = max(ans, d - ori);
            }
        } else if (!pre_out && suc_out){
            // cout << i << ' ' << 3333 << '\n';

            Point v = suc - sucsuc;
            Line l = Line(suc, Point(suc.x + v.y, suc.y - v.x));
            Point int_p;
            line_intersect(l, Line(prepre, pre), int_p);
            if (point_dist(mid, int_p) <= r){
                ld r = point_dist(mid, pre);
                ld d = point_to_line_dist(mid, Line(prepre, pre));
                ld x = 2*sqrtl(r*r - d*d);
                ld y = sqrtl((4*r*r) - x*x);
                ld ori = point_dist(pre, now) + point_dist(now, suc);
                ld dd = x + y;
                ans = max(ans, dd - ori);
            } else {
                ld r = point_dist(mid, pre);
                ld d = point_to_line_dist(mid, l);
                ld x = 2*sqrtl(r*r - d*d);
                ld y = sqrtl((4*r*r) - x*x);
                ld ori = point_dist(pre, now) + point_dist(now, suc);
                ld dd = x + y;
                ans = max(ans, dd - ori);
                r = point_dist(mid, suc);
                d = point_to_line_dist(mid, l2);
                x = 2*sqrtl(r*r - d*d);
                y = sqrtl((4*r*r) - x*x);
                ori = point_dist(pre, now) + point_dist(now, suc);
                dd = x + y;
                ans = max(ans, dd - ori);
            }

            if (is_ccw(l.s, l.t, circle_mid) && is_ccw(prepre, pre, circle_mid)){
                ld ori = point_dist(pre, now) + point_dist(now, suc);
                ld d = point_dist(pre, circle_mid) + point_dist(circle_mid, suc);
                ans = max(ans, d - ori);
            }
        } else {
            // cout << i << ' ' << 4444 << '\n';

            if (!ret){
                ld ori = point_dist(pre, now) + point_dist(now, suc);
                ld d = point_dist(pre, circle_mid) + point_dist(circle_mid, suc);
                ans = max(ans, d - ori);
                continue;
            }
            
            Point v = pre - prepre;
            Line l1 = Line(pre, Point(pre.x - v.y, pre.y + v.x));
            v = suc - sucsuc;
            Line l2 = Line(suc, Point(suc.x + v.y, suc.y - v.x));
            
            Point int_p;
            line_intersect(l1, l2, int_p);
            if (point_dist(mid, int_p) > r) continue;
            
            if (is_ccw(l2.s, l2.t, circle_mid) && is_cw(l1.s, l1.t, circle_mid)){
                ld ori = point_dist(pre, now) + point_dist(now, suc);
                ld d = point_dist(pre, circle_mid) + point_dist(circle_mid, suc);
                ans = max(ans, d - ori);
            }

            ld r = point_dist(mid, pre);
            ld d = point_to_line_dist(mid, l1);
            ld x = 2*sqrtl(r*r - d*d);
            ld y = sqrtl((4*r*r) - x*x);
            ld ori = point_dist(pre, now) + point_dist(now, suc);
            ld dd = x + y;
            ans = max(ans, dd - ori);
            r = point_dist(mid, suc);
            d = point_to_line_dist(mid, l2);
            x = 2*sqrtl(r*r - d*d);
            y = sqrtl((4*r*r) - x*x);
            ori = point_dist(pre, now) + point_dist(now, suc);
            dd = x + y;
            ans = max(ans, dd - ori);
        }
    }
   
    cout << fixed;
    cout.precision(30);
    cout << ans << '\n';
    
    return 0;
}