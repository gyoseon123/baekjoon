import math

def angle_from_center(point, center):
    return math.atan2(point[1] - center[1], point[0] - center[0])

def sort_points_counterclockwise(points):
    # 중심점 계산
    center = (
        sum([p[0] for p in points]) / len(points),
        sum([p[1] for p in points]) / len(points)
    )

    # 각도 계산 후 정렬
    points.sort(key=lambda p: angle_from_center(p, center))
    return points

# 테스트 좌표들
points = [(0, 0), (10, 0), (10, 5), (5 ,-1), (0, 5)]
sorted_points = sort_points_counterclockwise(points)
print("반시계 방향으로 정렬된 좌표들:", sorted_points)