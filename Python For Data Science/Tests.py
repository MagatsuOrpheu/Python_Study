A = set()
B = set()
A.add('x')
B.add('x')
A.add('Y')
B.add('z')
A.add('a')
B.add('b')

print(A)
print(B)

res = A.issuperset(B)
print(res)