import sys

def fac(n) :
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans


n, k = map(int, sys.stdin.readline().split())

print(fac(n)//fac(n-k)//fac(k))
