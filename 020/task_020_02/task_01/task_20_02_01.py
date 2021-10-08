import random

tup_s1 = tuple([random.randint(0, 5) for _ in range(10)])
tup_s2 = tuple([random.randint(-5, 0) for _ in range(10)])

print(tup_s1)
print(tup_s2)

tup_s3 = tup_s1 + tup_s2
print(tup_s3)
print(tup_s3.count(0))
