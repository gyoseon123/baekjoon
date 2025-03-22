# [Platinum V] Ponk Warshall - 18179 

[문제 링크](https://www.acmicpc.net/problem/18179) 

### 성능 요약

메모리: 115248 KB, 시간: 216 ms

### 분류

그리디 알고리즘

### 제출 일자

2025년 2월 24일 23:08:04

### 문제 설명

<p>Listening to the rock music permutes your nuclear DNA. This astonishing and unbelievable fact was recently published in the Rock Nature Weekly, one of the top scientific journals on the planet. Part of the research was to take DNA samples from volunteers, both before and after the rock concerts season. The samples were processed and various genes isolated from the samples. For each person, each gene was isolated twice: The variant before the rock season and the variant after the season. These two variants were paired and in many cases one variant was found to be some permutation of the other variant in the pair.</p>

<p>The next step in the research is to determine how the permutations happen. The prevalent hypothesis suggests that a permutation is composed of a sequence of transpositions, so-called swaps. A swap is an event (its chemistry is not fully understood yet) in which exactly two nucleobases in the gene exchange their places in the gene. No other nucleobases in the gene are affected by the swap. The positions of the two swapped nucleobases might be completely arbitrary.</p>

<p>To predict and observe the movement of the molecules in the permutation process, the researchers need to know the theoretical minimum number of swaps which can produce a particular permutation of nucleobases in a gene. We remind you that the nuclear DNA gene is a sequence of nucleobases cytosine, guanine, adenine, and thymine, which are coded as C, G, A, and T, respectively.</p>

### 입력 

 <p>The input contains two text lines. Each line contains a string of N capital letters “A”, “C”, “G”, or “T”, (1 ≤ N ≤ 10<sup>6</sup>). The two strings represent one pair of a particular gene versions. The first line represents the gene before the rock season, the second line represents the same gene from the same person after the rock season. The number of occurrences of each nucleobase is the same in both strings.</p>

### 출력 

 <p>Output the minimum number of swaps that transform the first gene version into the second one.</p>

