"""
Import from collections
# Deque é uma lista de alta performance
"""

from collections import deque

deq = deque('Orpheus')
print(deq)

deq.append('k')
print(deq)

deq.appendleft('k')
print(deq)

deq.pop()
print(deq)

deq.popleft()
print(deq)