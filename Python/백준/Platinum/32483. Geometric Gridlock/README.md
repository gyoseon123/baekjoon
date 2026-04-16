# [Platinum II] Geometric Gridlock - 32483 

[문제 링크](https://www.acmicpc.net/problem/32483) 

### 성능 요약

메모리: 32412 KB, 시간: 40 ms

### 분류

구현, 해 구성하기, 많은 조건 분기

### 제출 일자

2025년 2월 20일 23:38:11

### 문제 설명

<p><em>Pentominous</em> is a grid logic puzzle based on the twelve pentominoes. A pentomino is a polygon formed by connecting five equal-sized squares edge to edge.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/6990680e-5332-4114-ab51-af5025e03889/-/preview/" style="width: 367px; height: 200px;"></p>

<p style="text-align: center;">Figure G.1: The twelve pentominoes (up to mirroring and rotations) and their names.</p>

<p>The goal of this puzzle is to divide a grid into regions of size $5$ (that is, pentominoes), so that no two regions that share a side have the same shape. You are allowed to rotate and mirror the pentominoes, but such rotations and reflections count as the same shape. The twelve possible shapes can be seen in Figure \ref{fig:pentominoes}.</p>

<p>In a normal <em>Pentominous</em> puzzle, the player is given some pre-filled cells, for which the shape of their region is already predetermined. In this problem, you are working with a completely blank grid of dimensions $h\times w$, and your task is to create any valid arrangement of pentominoes.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line with two integers $h$ and $w$ ($1 \le h,w \le 100$), the height and width of the grid.</li>
</ul>

### 출력 

 <p>If there is no valid $h\times w$ <em>Pentominous</em> grid, output "<code>no</code>". Otherwise, output "<code>yes</code>", followed by $h$ lines of width $w$ each, a possible grid using the letters from Figure G.1. If there is more than one solution, any one of them will be accepted.</p>

