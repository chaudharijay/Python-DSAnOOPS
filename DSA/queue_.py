# queue = FIFO data structure. First In First Out

# dequeue = remove element
# enqueue = add element

queue = []
queue.append('a')
queue.append('b')
queue.append('c')
queue.append('d')
print(queue)  # ['a', 'b', 'c', 'd']

# now dequeue
print(queue.pop(0))
print(queue.pop(1))
print(queue)
