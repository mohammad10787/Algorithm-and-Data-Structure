# from collections import deque
# import time
# import threading
#
# class Queue:
#
#     def __init__(self):
#         self.buffer = deque()
#
#     def enqueue(self, orders):
#         for order in orders:
#             print("Placing order for:", order)
#             self.buffer.appendleft(order)
#             time.sleep(0.5)
#
#     def dequeue(self):
#         time.sleep(1)
#         while self.is_empty():
#             order = self.buffer.pop()
#             print("Now serving:", order)
#             time.sleep(2)
#
#
#     def is_empty(self):
#         return len(self.buffer)
#
#     def size(self):
#         return len(self.buffer)
#
# if __name__ == "__main__":
#     orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
#
#     pq = Queue()
#
#     t1 = threading.Thread(target=pq.enqueue, args=(orders,))
#     t2 = threading.Thread(target=pq.dequeue)
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()

from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]

def produce_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for i in range(n):
        front = numbers_queue.front()
        print("   ", front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")
        print(numbers_queue.buffer)

        numbers_queue.dequeue()
        print(numbers_queue.buffer)


if __name__ == '__main__':
    produce_binary_numbers(10)
