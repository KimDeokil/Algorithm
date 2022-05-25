import sys

n = int(sys.stdin.readline())
alpa = []

for i in range(n):
    alpa.append(sys.stdin.readline().strip())
alpa = list(set(alpa))
alpa.sort()
alpa.sort(key=len)

for j in alpa:
    print(j)
