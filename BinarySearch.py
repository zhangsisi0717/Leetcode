from bisect import bisect_left
from collections import deque
a = deque([2.5, 3, 6, 77, 334, 777])
bisect_left(a,2.6)
a.insert(1,2.6)

