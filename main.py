enum=int(input())
e=set(map(int,input().split()))
fnum=int(input())
f=set(map(int,input().split()))
a=e.union(f)
print(len(a))