# Salutes

Problem Description
 
 
In a long hallway some soldiers are walking from left to right and some from right to left all at the same speed.

Every time while walking they cross through another soldier they salute and move ahead.

Given a string A of length N showing the soldiers' direction they are walking. 
'<' denotes a soldier is walking from right to left, and '>' denotes a soldier is walking from left to right. 
Return the number of Salutes done.



Problem Constraints
1 <= N <= 105
A = {'<', '>'}


Input Format
The first argument is a string A.


Output Format
Return a single integer denoting the number of salutes done.


Example Input
Input 1:
A = '>>><<<'
Input 2:

A = '<>'


Example Output
Output 1:
9
Output 2:

0


Example Explanation
Explanation 1:
Soldier 1 will salute with 4, 5, 6. Same goes for soldier 2 and 3.
Hence, the total number of salutes is 9.
Explanation 2:

There will be no salutes as no two soldiers will cross each other.
