K = int(input())
r_no = list(input().split(' '))

x = set()
y = set()
for r in r_no:
    if r not in x:
        x.add(r)
        y.add(r)
    else:
        y.discard(r)
y = list(y)
print(y[0])