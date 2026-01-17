from collections import deque

queue = deque()

for i in range(120):  
    queue.append(i)

while len(queue) >= 100:
    print(f"Kolejka ma {len(queue)} elementów.")
    queue.popleft()  
