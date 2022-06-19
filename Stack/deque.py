from collections import deque


stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
stack.appendleft(4)
stack.pop()
stack.popleft()
print(stack)
