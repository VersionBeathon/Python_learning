# _*_ coding:utf-8 _*_
from collections import deque
q = deque(range(5))
print q
q.append(5)
q.appendleft(6)
print q
print q.pop()
print q.popleft()
print q
q.rotate(3) # 将第一个数字移动到目标位置
print q
q.rotate(-1)
print q