# [Platinum II] Apple Pie - 35397 

[문제 링크](https://www.acmicpc.net/problem/35397) 

### 성능 요약

메모리: 215596 KB, 시간: 284 ms

### 분류

그래프 이론, 많은 조건 분기, 오일러 경로

### 제출 일자

2026년 4월 4일 03:41:24

### 문제 설명

<p>Asdrubal likes writing sequences of integers and eating apple pie. Sometimes he does both things simultaneously. These days he is interested in sequences of a particular type. Given an integer $N \ge 2$, he wants to find a sequence such that each set of two different integers between $1$ and $N$ appears exactly once in adjacent positions of the sequence. Besides, no other integers can appear in the sequence.</p>

<p>For instance, for $N = 2$, there is a single set of two different integers between $1$ and $N$, which is the set $\{1, 2\}$. Thus, Asdrubal would be satisfied with the sequence $[1, 2]$. The only other possibility is the sequence $[2, 1]$.</p>

<p>For $N = 3$, there are three sets of two different integers between $1$ and $N$: $\{1, 2\}$, $\{1, 3\}$ and $\{2, 3\}$. In this case a valid sequence is $[2, 1, 3, 2]$, since the set $\{1, 2\}$ only appears in the first two positions, the set $\{1, 3\}$ only appears in the middle, and the set $\{2, 3\}$ only appears in the last two positions, with no other integers appearing in the sequence. On the other hand, the sequences $[2, 1, 3]$, $[2, 1, 3, 2, 1]$ and $[2, 1, 3, 2, 2]$ are invalid.</p>

<p>Asdrubal thinks he has just written one of his sequences for a certain $N$. He was about to check whether the sequence was actually valid, when some apple pie fell on the paper. The apple pie covered zero or more elements of the sequence, splitting the rest into two (possibly empty) parts, one on the left of the apple pie, and one on the right. Given the left and right portions of the sequence not covered by apple pie, you must determine whether the original full sequence could have been valid.</p>

### 입력 

 <p>The first line contains an integer $N$ ($2 \le N \le 1000$).</p>

<p>The next line contains an integer $P$ ($0 \le P \le 5 \cdot 10^5$) indicating the number of integers on the left of the apple pie, followed by those $P$ integers $L_1, L_2, \ldots, L_P$ $(1 \le L_i \le N$ for $i = 1, 2, \ldots, P)$.</p>

<p>The next line contains an integer $Q$ $(0 \le Q \le 5 \cdot 10^5)$ representing the number of integers on the right of the apple pie, followed by those $Q$ integers $R_1, R_2, \ldots, R_Q$ ($1 \le R_i \le N$ for $i = 1, 2, \ldots, Q$).</p>

<p>Both the left and right portions of the sequence are described from left to right.</p>

### 출력 

 <p>Output a single line with the uppercase letter “<code>Y</code>” if the original full sequence could have been valid, and the uppercase letter “<code>N</code>” otherwise.</p>

