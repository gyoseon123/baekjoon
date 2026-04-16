# [Diamond IV] Big Brother - 21048 

[문제 링크](https://www.acmicpc.net/problem/21048) 

### 성능 요약

메모리: 148128 KB, 시간: 480 ms

### 분류

기하학, 다각형의 넓이, 반평면 교집합

### 제출 일자

2025년 11월 7일 00:20:20

### 문제 설명

<p>You have come up with a new brilliant idea of automatically keeping track of how much (or little) your employees are working in the office: face recognition! By installing some advanced CCTV cameras in the office you will be able to automatically detect when the staff arrives or leaves, are taking breaks etc, thus reducing the need for manual administrative work. No more stamping clocks.</p>

<p>A good CCTV camera is expensive, so ideally you would only use one. It would obviously have to be placed somewhere where the entire office floor can be overlooked, so there are no walls blocking some dark corner of the floor where your workforce might hide.</p>

<p>While looking at the floor map, which can be modelled as a simple polygon, you are not sure if this is possible. Since the task is way above the paygrade of everyone else in the company you will have to write the program figuring this out yourself. If it is possible, you also want to know the area of the surface where the camera could be placed.  See Figure 1 for an example.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/bdf354b4-2a2b-47b8-a9b8-ebaab0045591/-/preview/" style="width: 374px; height: 499px;"></p>

<p style="text-align: center;">Figure 1: Illustration of Sample Input 3.  The blue shaded area in the middle indicates the region where the camera can be placed.</p>

### 입력 

 <p>The first line of input contains an integer $n$ ($3 \le n \le 500\,000$), the number of vertices describing the polygon representing the office floor. Then follow $n$ lines containing the integer coordinates $x, y$ of the polygon in clockwise order ($0 \le x, y \le 10^7$).</p>

### 출력 

 <p>Output the area of the region of the map where a CCTV camera could be placed so that the rest of the office can be observed. (If it is not possible to put the camera anywhere, this area is $0$.)</p>

<p>The answer must be correct with a relative of at most $10^{-6}$, or an absolute error of at most $0.1$.</p>

