<pre>
Newton's coding challenge January 2022 - Smallest string

standard input/output: 2s/128000 kB

Given N and K, find the lexicographically smallest string of length N using only the first K lowercase letters of the alphabet such that each letter is used at least once and no two adjacent characters are equal.

If such a string doesn't exist, print -1.

Input
The first line of input contains a single integer, T (1 <= T <= 100).

Then T lines follow, each containing two space-separated integers, N (1 <= N <= 105) and K (1 <= K <= 26).

It is guaranteed that sum of N over all test cases does not exceed 106

Output
For each test case, output its answer in a new line.

Example
Sample Input:
2
2 3
3 2

Sample Output:
-1
aba
</pre>

## [Solution](smallest%20string.py) 