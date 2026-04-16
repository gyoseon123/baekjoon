# [Diamond V] Engineering Excellence - 35088 

[문제 링크](https://www.acmicpc.net/problem/35088) 

### 성능 요약

메모리: 8316 KB, 시간: 56 ms

### 분류

기하학, 많은 조건 분기

### 제출 일자

2026년 1월 10일 00:33:43

### 문제 설명

<p>You are the engineer in charge of designing a wheel for a new space rover. As you do not have enough time to reinvent the wheel, you decide to copy your predecessor's work and make only one small change.</p>

<p>Looking at the plan, you notice that your predecessor's wheel has the shape of a convex polygon for structural reasons. It is well known that wheels with a larger perimeter roll farther per rotation, so surely they must be superior. You attempt to increase the perimeter by as much as possible by moving a single point on the outside of the wheel. While experimenting, you notice that wheels do not seem to work if they are non-convex or if there is an internal angle below $90$ degrees.</p>

<p>What is the maximum possible achievable increase in the perimeter of the wheel without violating the above restrictions?</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/e7fe89a9-ad92-45ac-9490-9c1ffac79384/-/preview/" style="width: 300px; height: 263px;"></p>

<p style="text-align: center;">Figure E.1: Visualization of the first sample. Point $3$ is moved to $(5.5, 3.5)$, increasing the perimeter by $\approx 1.59488$.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
<li>One line with an integer $n$ ($4 \leq n \leq 10^5$), the number of points of the wheel.</li>
<li>$n$ lines, each with two integers $x$ and $y$ ($\left| x \right|, \left| y \right| \leq 10^5$), the coordinates of the points.</li>
</ul>

<p>The points are given in counterclockwise order and form a convex polygon with no internal angle below $90$ degrees. Note that the convex polygon may contain <strong>collinear</strong> points, but no two points are at the same position.</p>

### 출력 

 <p>Output the maximum possible absolute increase of the perimeter of the wheel.</p>

<p>Your answer should have an absolute or relative error of at most $10^{-6}$.</p>

