# [Platinum IV] Hopscotch 500 - 24596 

[문제 링크](https://www.acmicpc.net/problem/24596) 

### 성능 요약

메모리: 17652 KB, 시간: 636 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2024년 8월 15일 18:00:54

### 문제 설명

<p>Do you remember the new art installation from NAC 2020? Well, that artist is at it again, on a grander scale this time, and the new artwork still inspires you---to play a childish game. The art installation consists of a floor with a square matrix of tiles. Each tile holds a single number from $1$ to $k$.</p>

<p>You want to play hopscotch on it! You want to start on some tile numbered $1$, then hop to a tile numbered $2$, then $3$, and so on, until you reach a tile numbered $k$.</p>

<p>Instead of the usual Euclidean distance, define the distance between the tile at $(x_1,y_1)$ and the tile at $(x_2,y_2)$ as: \[\min\left[(x_1-x_2)^2, (y_1-y_2)^2\right]\] You want to hop the shortest total distance overall, using this new distance metric. Note that a path with no hops is still a path, and has length $0$. What is the length of the shortest path?</p>

### 입력 

 <p>The first line of input contains two space-separated integers $n$ ($1 \le n \le 500$) and $k$ ($1\le k\le n^2$), where the art installation consists of an $n\!\times\! n$ matrix with tiles having numbers from $1$ to $k$.</p>

<p>Each of the next $n$ lines contains $n$ space-separated integers $x$ ($1 \le x \le k$). These are the numbers in the art installation.</p>

### 출력 

 <p>Output a single integer, which is the total length of the shortest path from any $1$ tile to any $k$ tile using our distance metric, or $-1$ if no such path exists.</p>

