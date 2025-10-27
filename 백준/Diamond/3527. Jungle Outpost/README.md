# [Diamond I] Jungle Outpost - 3527 

[문제 링크](https://www.acmicpc.net/problem/3527) 

### 성능 요약

메모리: 20080 KB, 시간: 424 ms

### 분류

기하학, 이분 탐색, 매개 변수 탐색, 반평면 교집합

### 제출 일자

2025년 10월 20일 02:31:26

### 문제 설명

<p>There is a military base lost deep in the jungle. It is surrounded by n watchtowers with ultrasonic generators. In this problem watchtowers are represented by points on a plane.</p>

<p>Watchtowers generate ultrasonic field and protect all objects that are strictly inside the towers’ convex hull. There is no tower strictly inside the convex hull and no three towers are on a straight line.</p>

<p>The enemy can blow up some towers. If this happens, the protected area is reduced to a convex hull of the remaining towers.</p>

<p style="text-align: center;"><img alt="" src="https://www.acmicpc.net/upload/images3/jungle.png" style="height:208px; width:616px"></p>

<p>The base commander wants to build headquarters inside the protected area. In order to increase its security, he wants to maximize the number of towers that the enemy needs to blow up to make the headquarters unprotected.</p>

### 입력 

 <p>The first line of the input file contains a single integer n (3 ≤ n ≤ 50 000) — the number of watchtowers. The next n lines of the input file contain the Cartesian coordinates of watchtowers, one pair of coordinates per line. Coordinates are integer and do not exceed 10<sup>6</sup> by absolute value. Towers are listed in the order of traversal of their convex hull in clockwise direction.</p>

### 출력 

 <p>Write to the output file the number of watchtowers the enemy has to blow up to compromise headquarters protection if the headquarters are placed optimally.</p>

