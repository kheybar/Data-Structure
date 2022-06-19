"""
queue wtih priority
"""
import heapq


q = []

heapq.heappush(q, (2, 'code'))
heapq.heappush(q, (1, 'eat'))
heapq.heappush(q, (3, 'sleep'))

for i in q:
    print(i)
