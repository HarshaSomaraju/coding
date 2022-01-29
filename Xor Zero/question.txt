Newton's coding challenge January 2022 - Xor Zero (Public Contest: January 2022)

Xor Zero (Public Contest: January 2022)

standard input/output: 2s/128000 kB

For a given positive integer N, determine if there exist three positive integers a, b and c such that the following two conditions hold:

1. a + b + c = N
2. a ^ b ^ c = 0 where ^ denotes the bitwise XOR operation.

If there exist such a triple (a, b, c), print the lexicographically smallest one.
Else, print -1.

Input
The first line of input contains a single integer, T.
T lines follow, each containing a single integer, N.

Constraints:

1 <= T <= 103
3 <= N <= 1018

Output
For each test, in a new line, print the lexicographically smallest triple (a, b, c) if it exists, else print -1.

Example

Sample Input:
3
3
6
12

Sample Output:
-1
1 2 3
2 4 6