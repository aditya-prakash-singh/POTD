# Amazing Subarrays

Problem Description
 
 

You are given a string A, and you have to find all the amazing substrings of A.
An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).
Note: Take the mod of the answer with 10003.


Problem Constraints
1 <= |S| <= 106
S can have special characters


Input Format
Only argument given is string S.


Output Format
Return a single integer X mod 10003, where X is the number of Amazing Substrings in the given string.


Example Input
ABEC


Example Output
6


Example Explanation
Amazing substrings of the given string are :
1. A
2. AB
3. ABE
4. ABEC
5. E
6. EC
here the number of substrings is 6 and 6 % 10003 = 6.
