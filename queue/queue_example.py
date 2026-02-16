from collections import deque

queue = deque()

queue.append("Task1")
queue.append("Task2")
queue.append("Task3")

print("Queue:", queue)

print("Served:", queue.popleft())
print("Remaining:", queue)
