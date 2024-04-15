def generateNextPalindromeUtil(num, n):
    mid = n // 2
    leftsmaller = False
    i = mid - 1
    j = mid + 1 if n % 2 else mid

    while i >= 0 and num[i] == num[j]:
        i -= 1
        j += 1

    if i < 0 or num[i] < num[j]:
        leftsmaller = True

    while i >= 0:
        num[j] = num[i]
        j += 1
        i -= 1

    if leftsmaller:
        carry = 1
        i = mid - 1
        if n % 2 == 1:
            num[mid] += carry
            carry = num[mid] // 10
            num[mid] %= 10
            j = mid + 1
        else:
            j = mid

        while i >= 0:
            num[i] += carry
            carry = num[i] // 10
            num[i] %= 10
            num[j] = num[i]
            j += 1
            i -= 1

    return num

def AreAll9s(num):
    for digit in num:
        if digit != 9:
            return False
    return True

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        kom=[int(om)for om in A]
        l=len(kom)
        ans=[]
        if AreAll9s(kom):
            ans.append(1)
            for i in range(1, l):
                ans.append(0)
            ans.append(1)
        else:
            ans = generateNextPalindromeUtil(kom, l)

        return ''.join(map(str,ans))
