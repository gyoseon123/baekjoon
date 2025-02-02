# [Platinum III] Shortest Common Non-Subsequence - 16742 

[문제 링크](https://www.acmicpc.net/problem/16742) 

### 성능 요약

메모리: 65976 KB, 시간: 108 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2025년 1월 21일 19:34:41

### 문제 설명

<p>A <em>subsequence</em> of a sequence P is a sequence that can be derived from the original sequence P by picking up some or no elements of P preserving the order. For example, “ICPC” is a subsequence of “<code>MICROPROCESSOR</code>”.</p>

<p>A common subsequence of two sequences is a subsequence of both sequences. The famous longest common subsequence problem is finding the longest of common subsequences of two given sequences.</p>

<p>In this problem, conversely, we consider <em>the shortest common non-subsequence problem</em>: Given two sequences consisting of 0 and 1, your task is to find the shortest sequence also consisting of 0 and 1 that is a subsequence of <em>neither</em> of the two sequences.</p>

### 입력 

 <p>The input consists of a single test case with two lines. Both lines are sequences consisting only of 0 and 1. Their lengths are between 1 and 4000, inclusive.</p>

### 출력 

 <p>Output in one line the shortest common non-subsequence of two given sequences. If there are two or more such sequences, you should output the lexicographically smallest one. Here, a sequence P is lexicographically smaller than another sequence Q of the same length if there exists k such that P<sub>1</sub> = Q<sub>1</sub>, . . . , P<sub>k−1</sub> = Q<sub>k−1</sub>, and P<sub>k</sub> < Q<sub>k</sub>, where S<sub>i</sub> is the i-th character of a sequence S.</p>

