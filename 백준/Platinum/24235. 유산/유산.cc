#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <climits>
#include <iomanip>

using namespace std;

struct Point {
    double x, y;
    bool operator<(const Point &other) const {
        if (x != other.x)
            return x < other.x;
        return y < other.y;
    }
};

double ccw(const Point &p1, const Point &p2, const Point &p3) {
    return (p2.x - p1.x)*(p3.y - p1.y) - (p3.x - p1.x)*(p2.y - p1.y);
}

double polygon_area(const vector<Point> &points) {
    int n = points.size();
    double area = 0;
    for (int i = 0; i < n; i++) {
        area += points[i].x * points[(i+1)%n].y;
        area -= points[(i+1)%n].x * points[i].y;
    }
    return fabs(area) / 2.0;
}

void convex_hull(const vector<Point> &points, vector<Point> &up, vector<Point> &down) {
    int n = points.size();
    vector<Point> sorted_points = points;
    sort(sorted_points.begin(), sorted_points.end());

    for (const auto &p : sorted_points) {
        while (up.size() >= 2 && ccw(up[up.size()-2], up.back(), p) >= 0)
            up.pop_back();
        up.push_back(p);

        while (down.size() >= 2 && ccw(down[down.size()-2], down.back(), p) <= 0)
            down.pop_back();
        down.push_back(p);
    }
}

struct Line {
    double a, b, c; // Line equation: a*x + b*y + c = 0
};

Line find_line(const Point &p1, const Point &p2) {
    if (p1.x - p2.x == 0) {
        return {1.0, 0.0, -p1.x};
    }
    double d = (p1.y - p2.y) / (p1.x - p2.x);
    return {d, -1.0, -d*p1.x + p1.y};
}

double find_y(const Line &line, double x) {
    return (-line.a * x - line.c) / line.b;
}

pair<vector<Point>, vector<Point>> up_find(const vector<Point> &up, double x) {
    int n = up.size();
    int idx = 0;
    for (int i = 0; i < n; i++) {
        if (x > up[i].x)
            idx = i;
    }
    if (idx >= n - 1) idx = n - 2; // Ensure idx + 1 < n
    Line line = find_line(up[idx], up[idx+1]);
    Point point = {x, find_y(line, x)};
    vector<Point> left(up.begin(), up.begin() + idx + 1);
    left.push_back(point);
    vector<Point> right;
    right.push_back(point);
    right.insert(right.end(), up.begin() + idx + 1, up.end());
    return {left, right};
}

pair<vector<Point>, vector<Point>> down_find(const vector<Point> &down, double x) {
    int n = down.size();
    int idx = 0;
    for (int i = 0; i < n; i++) {
        if (x > down[i].x)
            idx = i;
    }
    if (idx >= n - 1) idx = n - 2; // Ensure idx + 1 < n
    Line line = find_line(down[idx], down[idx+1]);
    Point point = {x, find_y(line, x)};
    vector<Point> left(down.begin(), down.begin() + idx + 1);
    left.push_back(point);
    vector<Point> right;
    right.push_back(point);
    right.insert(right.end(), down.begin() + idx + 1, down.end());
    return {left, right};
}

int main() {
    int n;
    cin >> n;
    vector<Point> points(n);
    double minX = INT_MAX, maxX = INT_MIN;
    for (int i = 0; i < n; i++) {
        cin >> points[i].x >> points[i].y;
        minX = min(minX, points[i].x);
        maxX = max(maxX, points[i].x);
    }

    vector<Point> up, down;
    convex_hull(points, up, down);

    double left = minX;
    double right = maxX;

    for (int iter = 0; iter < 50; iter++) {
        double mid = (left + right) / 2.0;

        auto up_split = up_find(up, mid);
        auto down_split = down_find(down, mid);

        vector<Point> left_side = up_split.first;
        vector<Point> downl_reversed = down_split.first;
        reverse(downl_reversed.begin(), downl_reversed.end());
        left_side.insert(left_side.end(), downl_reversed.begin(), downl_reversed.end());

        vector<Point> right_side = up_split.second;
        vector<Point> downr_reversed = down_split.second;
        reverse(downr_reversed.begin(), downr_reversed.end());
        right_side.insert(right_side.end(), downr_reversed.begin(), downr_reversed.end());

        double left_area = polygon_area(left_side);
        double right_area = polygon_area(right_side);

        if (left_area >= right_area) {
            right = mid;
        } else {
            left = mid;
        }
    }

    cout << fixed << setprecision(10) << left << endl;

    return 0;
}
