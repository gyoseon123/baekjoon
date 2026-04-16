# [Platinum I] Hidden Pancakes - 22911 

[문제 링크](https://www.acmicpc.net/problem/22911) 

### 성능 요약

메모리: 11324 KB, 시간: 4216 ms

### 분류

조합론, 다이나믹 프로그래밍, 트리에서의 다이나믹 프로그래밍, 수학, 트리

### 제출 일자

2025년 1월 18일 15:34:48

### 문제 설명

<p>We are cooking N pancakes in total. We cook one pancake with a 1 centimeter (cm) radius, one with a 2 cm radius, one with a 3 cm radius, ..., and one with an N cm radius, not necessarily in that order. After we cook the first pancake, we just lay it on a plate. After we cook each subsequent pancake, we lay it on top of the previously made pancake, with their centers coinciding. In this way, a pancake is visible from the top of the stack when we first add it. A pancake only becomes hidden if we later cook another pancake with a larger radius.</p>

<p>For example, say we cook 4 pancakes. We first cook the pancake with radius 3 cm, and it is visible. Then, we cook the pancake with radius 1 cm, lay it on top of the first one and both are visible. Third, we cook the pancake with radius 2 cm, and now that covers the previous pancake, but not the first one, so 2 pancakes remain visible in total. Finally, we cook the pancake with radius 4 cm which covers the other pancakes leaving only 1 visible pancake. The picture below illustrates the state of the stack after each pancake is cooked. Within each stack, the fully colored pancakes are visible and the semi-transparent pancakes are not visible.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 400px; height: 139px;"></p>

<p>Let V<sub>i</sub> be the number of visible pancakes when the stack contains exactly i pancakes. In the example above, V<sub>1</sub> = 1, V<sub>2</sub> = 2, V<sub>3</sub> = 2, and V<sub>4</sub> = 1.</p>

<p>Given the list V<sub>1</sub>, V<sub>2</sub>, …, V<sub>N</sub>, how many of the N! possible cooking orders yield those values? Since the output can be a really big number, we only ask you to output the remainder of dividing the result by the prime 10<sup>9</sup>+7 (1000000007).</p>

### 입력 

 <p>The first line of the input gives the number of test cases, T. T test cases follow, each described with two lines. The first line of a test case contains a single integer N, the number of pancakes we cook. The second line of a test case contains N integers V<sub>1</sub>, V<sub>2</sub>, ..., V<sub>N</sub>, representing the number of visible pancakes after we cook 1, 2, ..., N pancakes, respectively.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the number of cooking orders of N pancakes that yield the given numbers of visible pancakes after each step, modulo the prime 10<sup>9</sup>+7 (1000000007).</p>

