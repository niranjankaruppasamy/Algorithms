from collections import namedtuple


a = namedtuple("person", ["name", "age", "salary"])

a1 = a("Niranjan", "24", "50000")

print(a1.name)

import heapq

l1 = [4,6,2,8,0,1]

heapq.heapify(l1)

print(list(l1))

print(heapq.heappop(l1))
print(list(l1))


