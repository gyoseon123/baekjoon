from functools import cmp_to_key 
import sys
input = sys.stdin.readline

def ccw():
    pass

def find_convex_hull(points):
    points.sort()


n,px,py = map(int, input().split())
point = [tuple(map(int, input().split())) for _ in range(n)]
point.append((px, py))
