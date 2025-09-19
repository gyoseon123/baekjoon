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
bool is_ccw(Point p1, Point p2, Point p3){return (p2.x - p1.x)*(p3.y - p1.y) - (p3.x - p1.x)*(p2.y - p1.y) >= -1e-9;}
bool is_equal(ld a, ld b){return abs(a - b) < 1e-9;}

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
    return (crs < 1e-9);
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

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<Point> p;
    int n; cin >> n;
    for (int i = 0; i < n; i++){
        int x,y; cin >> x >> y;
        Point tmp;
        tmp.x = x;
        tmp.y = y;
        p.push_back(tmp);
    }

    vector<Line> lines;
    reverse(p.begin(), p.end());

    for (int i = 0; i < n; i++){
        Point p1 = p[i%n];
        Point p2 = p[(i+1)%n];
        Line l;
        l.s = p1;
        l.t = p2;
        lines.push_back(l);
    }

    vector<Point> hpi = HPI(lines);
    cout << fixed;
    cout.precision(10);
    cout << find_area(hpi) << '\n';
    
    return 0;
}