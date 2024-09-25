# [Gold III] Wet Tiles - 10349 

[문제 링크](https://www.acmicpc.net/problem/10349) 

### 성능 요약

메모리: 241568 KB, 시간: 1692 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2024년 9월 25일 16:40:39

### 문제 설명

<p>Alice owns a construction company in the town of Norainia, famous for its unusually dry weather. In fact, it only rains a few days per year there. Because of this phenomenon, many residents of Norainia neglect to do roof repairs until leaks occur and ruin their floors. Every year, Alice receives a deluge of calls from residents who need the leaks fixed and floor tiles replaced. While exquisite in appearance, Norainia floor tiles are not very water resistant; once a tile becomes wet, it is ruined and must be replaced. This year, Alice plans to handle the rainy days more efficiently than in past years. She will hire extra contractors to dispatch as soon as the calls come in, so hopefully all leaks can be repaired as soon as possible. For each house call, Alice needs a program to help her determine how many replacement tiles a contractor team will need to bring to complete the job.</p>

<p>For a given house, square floor tiles are arranged in a rectangular grid. Leaks originate from one or more known source locations above specific floor tiles. After the first minute, the tiles immediately below the leaks are ruined. After the second minute, water will have spread to any tile that shares an edge with a previously wet tile. This pattern of spreading water continues for each additional minute. However, the walls of a house restrict the water; if a damaged area hits a wall, the water does not penetrate the wall. We assume there are always four outer walls surrounding the entire house. A house may also have a number of additional "inner" walls; each inner wall is comprised of a connected linear sequence of locations (which may or may not be connected to the outer walls or to each other).  <!-- The footprint of the walls do not get wet. --></p>

<p>As an example, Figure 1 shows water damage (in gray) that would result from three initial leaks (each marked with a white letter 'L') after each of the first five minutes of time. Tiles labeled '2' become wet during the second minute, tiles labeled '3' become wet during the third minute, and so forth. The black areas designate inner walls that restrict the flow of water. Note that after 5 minutes, a total of 75 tiles have been damaged and will need to be replaced. Figures 2 through 4 show other houses that correspond to the example inputs for this problem.</p>

<table style="height:204px; text-align:center; width:406px">
	<tbody>
		<tr>
			<td><img alt="example 1" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/10349/1.png" style="height:272px; width:273px"><br>
			75 wet tiles</td>
		</tr>
		<tr>
			<td>Figure 1</td>
		</tr>
	</tbody>
</table>

<table style="height:204px; text-align:center; width:406px">
	<tbody>
		<tr>
			<td><img alt="example 2" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/10349/2.png" style="height:183px; width:223px"><br>
			17 wet tiles</td>
			<td><img alt="example 3" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/10349/3.png" style="height:179px; width:155px"><br>
			4 wet tiles</td>
			<td><img alt="example 4" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/10349/4.png" style="height:186px; width:182px"><br>
			94 wet tiles</td>
		</tr>
		<tr>
			<td>Figure 2</td>
			<td>Figure 3</td>
			<td>Figure 4</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>Each house is described beginning with a line having five integral parameters: <em>X Y T L W</em>. Parameters <em>X</em> and <em>Y</em> designate the dimensions of the rectangular grid, with 1 ≤ <em>X</em> ≤ 1000 and 1 ≤ <em>Y</em> ≤ 1000. The coordinate system is one-indexed, as shown in the earlier figures. Parameter <em>T</em> designates the number of minutes that pass before a team of contractors arrives at a house and stops the leaks, with 1 ≤ <em>T</em> ≤ 200000. The parameter <em>L</em> designates the number of leaks, with 1 ≤ <em>L</em> ≤ 100.  Parameter <em>W</em> designates the number of inner walls in the house, 0 ≤ W ≤ 100.</p>

<p>The following <em>2L</em> integers in the data set, on one or more lines, are distinct (x y) pairs that designate the locations of the <em>L</em> distinct leaks, such that 1 ≤ x ≤ X and 1 ≤ y ≤ Y.</p>

<p>If <em>W > 0</em>, there will be <em>4W</em> additional integers, on one or more lines, that describe the locations of the walls. For each such wall the four parameters <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D466 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msub><mi>y</mi><mn>1</mn></msub><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\((x_1, y_1)\)</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D466 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><msub><mi>y</mi><mn>2</mn></msub><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\((x_2, y_2)\)</span></mjx-container> describe the locations of two ends of the wall.  Each wall replaces a linear sequence of adjoining tiles and is either axis-aligned or intersects both axes at a 45 degree angle.  Diagonal walls are modeled as a sequence of cells that would just be touching corner to corner.  If the two endpoints of a wall are the same, the wall just occupies the single cell at that location. Walls may intersect with each other, but no leak is over a wall.</p>

<p>There will be one or more houses in the data file and a line with a single integer <kbd>-1</kbd> designates the end of the data set.</p>

### 출력 

 <p>For each house, display the total number of tiles that are wet after <em>T</em> minutes.</p>

