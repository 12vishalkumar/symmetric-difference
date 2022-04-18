# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
A = set(map(int, input().split()))
N = int(input())
B = set(map(int, input().split()))

A1 = A.difference(B)
B1 = B.difference(A)
res = A1.union(B1)
res = sorted(res)
for i in res:
    print(i)