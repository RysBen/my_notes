#1.从可迭代对象中分解变量
##
lst=[1,(2,3)]
a,(b,c)=lst
##variable length
lst=list(range(10))
f,*m,l=lst

#2.保存最后N个元素；从队列末端添加和移除元素的复杂度O(1)，列表中O(N)
from collections import deque
q=deque(maxlen=2)
q.append(1);q.append(2)
q.appendleft(0)
q.pop()
q.popleft()

#3.找到最大或最小的N个元素
import random
lst=random.sample(range(100),20)
##N=1
print(min(lst))
print(max(lst))
##N << length
import heapq
print(heapq.nsmallest(n,lst))
print(heapq.nlargest(n,lst))
##N is near length
print(sorted(lst)[:n])
print(sorted(lst)[-n:])

