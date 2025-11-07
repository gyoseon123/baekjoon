# [Platinum III] Dishwashing - 17034 

[문제 링크](https://www.acmicpc.net/problem/17034) 

### 성능 요약

메모리: 9368 KB, 시간: 1520 ms

### 분류

이분 탐색, 자료 구조, 그리디 알고리즘, 구현, 스택

### 제출 일자

2025년 11월 7일 15:06:17

### 문제 설명

<p>Bessie and Elsie are helping Farmer John wash the dishes, a more complicated process than one might think due to their lack of opposable thumbs.</p>

<p>The two cows decide that Bessie will apply soap, and Elsie will rinse. Bessie is given a dirty stack of plates labeled <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container> through <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><msup><mn>10</mn><mn>5</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq N \leq 10^5$</span></mjx-container>) Elsie has an empty stack, where clean plates will go. There is a counter in between Bessie and Elsie for soapy stacks.</p>

<p>At each step, either:</p>

<ul>
	<li>Bessie takes a plate from the top of the dirty stack, applies soap, and then places it on the counter. When placing a soapy plate on the counter, Bessie must either (i) place the plate on top of an existing non-empty soapy stack or (ii) create a new soapy stack to the right of all existing soapy stacks.</li>
	<li>Elsie takes a plate from the top of the leftmost soapy stack. Elsie rinses the plate, then places it on top of the clean stack.</li>
</ul>

<p>The goal is for the clean stack to have all plates in order, with the smallest label on the bottom and the largest label on the top. It may not be possible for the cows to achieve this goal for the entire stack of plates, so please determine the length of the largest prefix of the input ordering for which the goal is achievable.</p>

### 입력 

 <p>The first line of input contains <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>. The next <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> lines specify the order of the dishes in Bessie's stack, with the first number being the dish on top of the stack.</p>

### 출력 

 <p>Please output the length of the longest prefix of the input stack that can be successfully washed so that the plates end up ordered properly in the clean stack.</p>

