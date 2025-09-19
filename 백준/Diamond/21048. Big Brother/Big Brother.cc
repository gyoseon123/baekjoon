#include <bits/stdc++.h>

#define ld long double
#define sz(x) ((int)x.size())

using namespace std;

struct Point{
    ld x,y;
    Point(){}
    Point(ld x, ld y) : x(x), y(y) {}
};

struct Line{
    Point s,t;
    Line(){}
    Line(Point s, Point t) : s(s), t(t) {}
};

bool is_equal(ld a, ld b){ return abs(a - b) < 1e-9; }

bool is_ccw(Point p1, Point p2, Point p3){
    return (p2.x - p1.x)*(p3.y - p1.y) - (p3.x - p1.x)*(p2.y - p1.y) >= -1e-9;
}

bool line_intersect(const Line& l1, const Line& l2, Point& p){
    ld dx1 = l1.t.x - l1.s.x;
    ld dy1 = l1.t.y - l1.s.y;
    ld dx2 = l2.t.x - l2.s.x;
    ld dy2 = l2.t.y - l2.s.y;
    ld det = dx1 * dy2 - dx2 * dy1;
    if (is_equal(det, 0)) return false;
    ld s = ((l2.s.x - l1.s.x) * dy2 - (l2.s.y - l1.s.y) * dx2) / det;
    p.x = l1.s.x + dx1 * s;
    p.y = l1.s.y + dy1 * s;
    return true;
}

bool is_hide(const Line& a, const Line& b, const Line& c) {
    Point v;
    if(!line_intersect(a, b, v)) return false;
    ld crs = (c.t.x-c.s.x)*(v.y-c.s.y)-(c.t.y-c.s.y)*(v.x-c.s.x);
    return crs < -1e-9;
}

ld find_area(const vector<Point>& points){
    if (points.size() < 3) return 0;
    ld area = 0.0;
    for (int i = 0; i < points.size(); i++) {
        Point p1 = points[i];
        Point p2 = points[(i + 1) % points.size()];
        area += (p1.x * p2.y - p2.x * p1.y);
    }
    return abs(area) / 2.0;
}

vector<Point> HPI(vector<Line>& lines) {
    auto line_div = [&](const Line& l){
        if (is_equal(l.s.y, l.t.y)) return l.s.x > l.t.x;
        return l.s.y > l.t.y;
    };
    sort(lines.begin(), lines.end(), [&](const Line& l1, const Line& l2){
        bool div1 = line_div(l1), div2 = line_div(l2);
        if (div1 != div2) return div1 < div2;
        ld crs = (l1.t.x - l1.s.x) * (l2.t.y - l2.s.y) - (l1.t.y - l1.s.y) * (l2.t.x - l2.s.x);
        if (!is_equal(crs, 0)) return crs > 1e-9;
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

    deque<Line> dq;
    for (const auto& line : unique_lines) {
        while (dq.size() >= 2 && is_hide(dq[dq.size()-2], dq.back(), line)) dq.pop_back();
        while (dq.size() >= 2 && is_hide(dq[0], dq[1], line)) dq.pop_front();
        dq.push_back(line);
    }

    while (dq.size() >= 2 && is_hide(dq[dq.size()-2], dq.back(), dq[0])) dq.pop_back();
    while (dq.size() >= 2 && is_hide(dq.back(), dq[0], dq[1])) dq.pop_front();

    vector<Point> ret;
    if (dq.size() >= 3){
        for (int i = 0; i < dq.size(); i++){
            int j = (i + 1) % dq.size();
            Point p;
            if (!line_intersect(dq[i], dq[j], p)) continue;
            ret.push_back(p);
        }
    }
    return ret;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n; cin >> n;
    vector<Point> p(n);
    for (int i = 0; i < n; i++){
        cin >> p[i].x >> p[i].y;
    }

    reverse(p.begin(), p.end());

    vector<Line> lines;
    for (int i = 0; i < n; i++){
        lines.push_back(Line(p[i], p[(i+1)%n]));
    }
    
    ld M = 2e9; 
    lines.push_back(Line(Point(-M, -M), Point(M, -M)));
    lines.push_back(Line(Point(M, -M), Point(M, M)));
    lines.push_back(Line(Point(M, M), Point(-M, M)));
    lines.push_back(Line(Point(-M, M), Point(-M, -M)));

    vector<Point> hpi_points = HPI(lines);

    cout << fixed << setprecision(10);
    cout << find_area(hpi_points) << '\n';
    
    return 0;
}