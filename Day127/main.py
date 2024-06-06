def max_sum(a,n):
    b=sum(a)
    c=sum(i*a[i] for i in range(n))
    ans=c
    for i in range(1,n):
        c=c+b-n*a[n-i]
        if c>ans:
            ans=c
    return ans