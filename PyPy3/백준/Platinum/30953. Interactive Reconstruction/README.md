# [Platinum II] Interactive Reconstruction - 30953 

[문제 링크](https://www.acmicpc.net/problem/30953) 

### 성능 요약

메모리: 17332 KB, 시간: 328 ms

### 분류

그래프 이론, 애드 혹, 트리, 비트마스킹

### 제출 일자

2025년 3월 3일 00:11:38

### 문제 설명

<p>This is an interactive task where your program will communicate with a grader through standard input and output. Your task is to reconstruct a labelled tree with $N$ nodes and $N-1$ edges. Nodes are labelled from $1$ to $N$.</p>

<p>Your program is allowed to make a few queries of the following type: Your program should print a string of $N$ characters, consisting only of zeros and ones, one corresponding to each node. The grader will return a sequence of $N$ space-separated integers, the $i$-th representing the sum of the values (i.e. digits of the query string) of all neighbours of the $i$-th node. That is, if node $j$ is a neighbour of node $i$, then the $j$-th digit of the query string counts towards the sum in the $i$-th number of the grader's answer.</p>

<p>See the example below for an illustration.</p>

### 입력 

 Empty

### 출력 

 Empty

