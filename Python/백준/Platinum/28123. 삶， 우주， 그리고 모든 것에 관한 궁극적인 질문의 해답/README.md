# [Platinum I] 삶, 우주, 그리고 모든 것에 관한 궁극적인 질문의 해답 - 28123 

[문제 링크](https://www.acmicpc.net/problem/28123) 

### 성능 요약

메모리: 31120 KB, 시간: 48 ms

### 분류

수학, 애드 혹

### 제출 일자

2024년 6월 9일 01:47:53

### 문제 설명

<p>$2^n$은 십진법으로 표기했을 때 $k$자리 수이고, 가장 높은 자리의 숫자는 $x$이다.</p>

<p>양의 정수 $n$, $k$, $x$가 주어질 때, $1$부터 $2^n$까지의 정수 중 <span style="color:#e74c3c;"><code><strong>4</strong></code></span>로 시작하는 <strong><span style="color:#e74c3c;"><code>2</code></span></strong>의 거듭제곱수의 개수를 구해 보자.</p>

### 입력 

 <p>첫째 줄에 양의 정수 $n$, $k$, $x$가 주어진다. ($1 \le n, k \le 10^{18};$ $1 \le x \le 9;$ $x \times 10^{k-1} \le 2^n \lt (x + 1) \times 10^{k-1}$)</p>

<p>$|2^n/10^{k-1} - x - 0.5| \lt 0.5 - 10^{-6}$인 경우만 주어진다.</p>

### 출력 

 <p>$1$부터 $2^n$까지의 정수 중 <span style="color:#e74c3c;"><code><strong>4</strong></code></span>로 시작하는 <strong><span style="color:#e74c3c;"><code>2</code></span></strong>의 거듭제곱수의 개수를 출력한다.</p>

