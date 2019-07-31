import itertools
print(len(list(itertools.permutations(range(10), 4))))

a = [0,1,2,3,4,5]

for ix, x in enumerate(a):
  print(ix, x, a)
  if x % 2 == 0:
    a.remove(x)