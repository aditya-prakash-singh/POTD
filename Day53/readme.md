# Divisible by 60


Problem Description
 
Given a large number represent in the form of an integer array A, where each element is a digit.

You have to find whether there exists any permutation of the array A such that the number becomes divisible by 60.

Return 1 if it exists, 0 otherwise.



Problem Constraints
1 <= |A| <= 105
0 <= Ai <= 9


Input Format
The first argument is an integer array A.


Output Format
Return a single integer '1' if there exists a permutation, '0' otherwise.


Example Input
Input 1:
A = [0, 6]
Input 2:

A = [2, 3]


Example Output
Output 1:
1
Output 2:

0


Example Explanation
Explanation 1:
We can rearrange the digits to form 60, which is divisible by 60.
Explanation 2:

There are only two possible permutations: [23, 32].
Both of them are not divisible by 60.
