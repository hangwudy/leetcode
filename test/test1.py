import heapq as hq

a = []

hq.heapify(a)
for i in range(10, 0, -1):
    hq.heappush(a, -i)
for i in range(10, 0, -1):
    hq.heappush(a, -i)
# print(list((reversed(a))))
while a:
    print(-hq.heappop(a))

b = [i for i in -hq.heappop(a)]
print(b)
