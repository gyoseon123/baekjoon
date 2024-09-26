# [Gold II] Omar’s Bug - 9642 

[문제 링크](https://www.acmicpc.net/problem/9642) 

### 성능 요약

메모리: 110404 KB, 시간: 100 ms

### 분류

분류 없음

### 제출 일자

2024년 9월 26일 11:21:51

### 문제 설명

<p>Omar is the youngest programer in the world, he is just 11 months old. He has read about the binary search algorithm, and he decided to write it by himself.</p>

<p>He wrote the following function (its syntax is valid and it does the same job in both C++ and Java):</p>

<div><div id="highlighter_830416" class="syntaxhighlighter  c"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div><div class="line number6 index5 alt1">6</div><div class="line number7 index6 alt2">7</div><div class="line number8 index7 alt1">8</div><div class="line number9 index8 alt2">9</div><div class="line number10 index9 alt1">10</div><div class="line number11 index10 alt2">11</div><div class="line number12 index11 alt1">12</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="c color1 bold">int</code> <code class="c plain">findFirstGreaterThanOrEqual(</code><code class="c color1 bold">int</code> <code class="c plain">array[], </code><code class="c color1 bold">int</code> <code class="c plain">N, </code><code class="c color1 bold">int</code> <code class="c plain">X) {</code></div><div class="line number2 index1 alt1"><code class="c spaces">    </code><code class="c color1 bold">int</code> <code class="c plain">start = 0, end = N;</code></div><div class="line number3 index2 alt2"><code class="c spaces">    </code><code class="c keyword bold">while</code> <code class="c plain">(start < end) {</code></div><div class="line number4 index3 alt1"><code class="c spaces">        </code><code class="c color1 bold">int</code> <code class="c plain">middle = (start + end) / 2;</code></div><div class="line number5 index4 alt2"><code class="c spaces">        </code><code class="c keyword bold">if</code> <code class="c plain">(array[middle] > X) {</code></div><div class="line number6 index5 alt1"><code class="c spaces">            </code><code class="c plain">end = middle;</code></div><div class="line number7 index6 alt2"><code class="c spaces">        </code><code class="c plain">} </code><code class="c keyword bold">else</code> <code class="c plain">{</code></div><div class="line number8 index7 alt1"><code class="c spaces">            </code><code class="c plain">start = middle + 1;</code></div><div class="line number9 index8 alt2"><code class="c spaces">        </code><code class="c plain">}</code></div><div class="line number10 index9 alt1"><code class="c spaces">    </code><code class="c plain">}</code></div><div class="line number11 index10 alt2"><code class="c spaces">    </code><code class="c keyword bold">return</code> <code class="c plain">start;</code></div><div class="line number12 index11 alt1"><code class="c plain">}</code></div></div></td></tr></tbody></table></div></div>

<p>The function will always be called with parameters which satisfy the following conditions:</p>

<ol>
	<li>The first parameter is an array which contains at least 1 integer and at most 99 integers.</li>
	<li>The array contains distinct integers and it is sorted in increasing order.</li>
	<li>The integers in the array are positive and each one is at most 100.</li>
	<li>N is the number of elements in this array.</li>
	<li>X is a positive integer which is at most 100.</li>
</ol>

<p>Here is how Omar wants the function to work:</p>

<p>If there is no integer in the given array which is greater than or equal to X , Omar wants the function to return N . Otherwise, Omar wants the function to return the index of the smallest integer in the array that is greater than or equal to X (the first element in the array has index 0).</p>

<p>Unfortunately there is a bug in the function and it returns wrong result for some cases, and Omar can not find the bug (he is too young). Can you help him to generate some arrays to test his function?</p>

### 입력 

 <p>Your program will be tested on one or more test cases. The first line of the input will be a single integer T, the number of test cases (1 ≤ T ≤ 100). Followed by the test cases, each test case is described in one line which contains 3 integers separated by a single space N X Y (1 ≤ N ≤ 99), (1 ≤ X ≤ 100) and (1 ≤ Y ≤ 2). N is the value of the second parameter and X is the value of the third parameter. If Y is 1, you should generate an array which when passed to the function with the given parameters, the function will return a correct result. If Y is 2, you should generate an array which when passed to the function with the given parameters, the function will return a wrong result. In both cases, the generated array must satisfy the above conditions.</p>

<p>Note that correct or wrong result is relative to the way which Omar wants the function to work.</p>

### 출력 

 <p>For each test case, print on a single line, N integers separated by a single space, the first integer is the first integer in the generated array, the second integer is the second integer in the generated array and so on (the generated array should satisfy the above conditions). If there is more than one correct solution, print the lexicographically smallest one.</p>

<p>When comparing two different arrays of the same length, the lexicographically smaller array is the one with a smaller value on the smallest index where they differ.</p>

