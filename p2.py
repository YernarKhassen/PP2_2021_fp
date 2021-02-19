a = list(map(int,input().split()))
n = int(input())
n%=len(a)
if n < 0:
    n = abs(n)
    print(*(a[n:] + a[0:n]))
else:
    print(*(a[-n:] + a[0:-n]))
