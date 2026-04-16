#include <bits/stdc++.h>
#define ll long long
#define ld long double
#define sz(x) ((int)x.size())
//#define int long long
const int inf = 1e9;
using namespace std;

struct Point{
    ld x,y;
    Point(){}
    Point(ld x, ld y){this->x = x, this->y = y;}
};

struct Line{
    Point s,t;
    Line(){}
    Line(Point s, Point t){this->s = s, this->t = t;}
};

ld cross(Point p1, Point p2, Point p3){return (p2.x - p1.x)*(p3.y - p1.y) - (p3.x - p1.x)*(p2.y - p1.y);}
bool is_ccw(Point p1, Point p2, Point p3){return (p2.x - p1.x)*(p3.y - p1.y) - (p3.x - p1.x)*(p2.y - p1.y) >= 0;}
bool is_equal(ld a, ld b){return abs(a - b) < 1e-12;}

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

bool line_intersect(Line l1, Line l2, Point& p){
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

bool is_hide(Line a, Line b, Line c){
    Point p;
    if (!line_intersect(a, b, p)) return 0;
    ld crs = cross(c.s, c.t, p);
    return (crs < 0);
}

ld find_area(vector<Point> points){
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

bool check(ld r, const vector<Line>& lines){
    vector<Line> new_lines;
    for (int i = 0; i < sz(lines); i++){
        new_lines.push_back(inner_line(lines[i], r));
    }
    vector<Point> hpi = HPI(new_lines);
    if (!is_equal(find_area(hpi), 0)) return true;
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
    cout.precision(10);
    cout << left << '\n';
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    while (1) {
        int n; cin >> n;
        if (n == 0) break;
        solve(n);
    }
    
    return 0;
}