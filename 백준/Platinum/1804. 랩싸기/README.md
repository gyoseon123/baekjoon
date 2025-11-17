# [Platinum III] 랩싸기 - 1804 

[문제 링크](https://www.acmicpc.net/problem/1804) 

### 성능 요약

메모리: 18120 KB, 시간: 60 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2025년 11월 17일 22:07:20

### 문제 설명

<p>조교들은 회식을 끝내고 많은 음식들이 남게 됐다. 그래서 조교는 이 남은 음식물을 랩에 싸서 보관하기로 결정했다.</p>

<p>N개의 음식물들이 2*B 격자에 흩어져서 배치되어 있다. 그리고 랩은 오직 직사각형 모양으로만 쌀 수 있다.</p>

<p>우리에겐 K개의 랩이 있다. 랩은 마음대로 늘릴 수 있기 때문에 한 랩의 가로, 세로 너비 제한은 없다.</p>

<table class="table table-bordered" style="width:45%">
	<tbody>
		<tr>
			<td style="width:5%"> </td>
			<td style="width:5%">김치</td>
			<td style="width:5%"> </td>
			<td style="width:5%"> </td>
			<td style="width:5%"> </td>
			<td style="width:5%">회</td>
			<td style="width:5%">회</td>
			<td style="width:5%">족발</td>
			<td style="width:5%">족발</td>
		</tr>
		<tr>
			<td style="width:5%"> </td>
			<td style="width:5%">라면</td>
			<td style="width:5%">라면</td>
			<td style="width:5%">라면</td>
			<td style="width:5%"> </td>
			<td style="width:5%"> </td>
			<td style="width:5%"> </td>
			<td style="width:5%"> </td>
			<td style="width:5%"> </td>
		</tr>
	</tbody>
</table>

<p>위와 같이 음식이 남았을 때는 김치와 라면을 2*3 모양으로 싸고, 회와 족발을 1*4 모양으로 싸면 총 랩을 싸야하는 면적이 10이 된다.</p>

<p>문제는 이렇게 음식들의 위치가 주어졌을 때 모든 음식을 싸기 위해 필요한 랩의 최소 면적을 구하는 것이다.</p>

### 입력 

 <p>첫째 줄에 N(1 ≤ N ≤ 1,000), K(1 ≤ K ≤ N), B(1 ≤ B ≤ 15,000,000)가 공백으로 구분되어 입력된다. 다음 N개의 줄에 음식이 있는 위치가 주어진다.</p>

### 출력 

 <p>모든 음식을 싸기 위해 필요한 랩의 최소 면적을 출력한다.</p>

