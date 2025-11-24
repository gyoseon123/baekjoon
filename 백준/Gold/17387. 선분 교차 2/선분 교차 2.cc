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

ostream& operator<<(ostream& os, const Point& p){ // 구조체 출력 정의 (디버깅용)
    os << p.x << ' ' << p.y;
    return os;
}

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
ld find_area(vector<Point> &points){ // 다각형 넓이반환, points는 cw 혹은 ccw일것
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

int is_in(vector<Point> &convex_hull, Point p){ // 내부 점 판정, ch는 ccw순일것
    int cnt = 0;
    int s = sz(convex_hull);
    for (int i = 0; i < s; i++){
        int dir = cross(convex_hull[i], convex_hull[(i+1)%s], p);
        if (dir > 0) cnt++;
        if (dir == 0){
            vector<Point> points = {convex_hull[i], convex_hull[(i+1)%s], p};
            sort(points.begin(), points.end());
            if (points[1] == p) cnt++;
        }
    }
    return cnt == s;
}

int is_cross(Point p1, Point p2, Point p3, Point p4){ // p1-p2 선분과 p3-p4선분이 교차하는지 판정
    ld dir1 = cross(p1, p2, p3)*cross(p1, p2, p4);
    ld dir2 = cross(p3, p4, p1)*cross(p3, p4, p2);
    
    // cout << dir1 << ' ' << dir2 << '\n';
    if (is_equal(dir1, 0) && is_equal(dir2, 0)){
        if (p1 < p2) swap(p1, p2);
        if (p3 < p4) swap(p3, p4);
        
        return (p3 <= p2 && p1 <= p4) || (p2 <= p3 && p4 <= p1);
    }
    return dir1 <= 0 && dir2 <= 0;
}

ld point_to_line_dist(Point p, Line line){ // 점과 직선 사이의 거리
    Point v = line.t - line.s;
    Line l = Line(p, Point(p.x - v.y, p.y + v.x));
    Point int_p;
    line_intersect(line, l, int_p);
    return point_dist(int_p, p);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // int n,k,h,m; cin >> n >> k >> h >> m;
    // vector<Point> wall;
    // for (int i = 0; i < n; i++){
    //     int x,y; cin >> x >> y;
    //     wall.push_back(Point(x,y));
    // }

    // for (int i = 0; i < )

    int x1,y1,x2,y2; cin >> x1 >> y1 >> x2 >> y2;
    int x3,y3,x4,y4; cin >> x3 >> y3 >> x4 >> y4;
    cout << is_cross(Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4));
    
    return 0;
}