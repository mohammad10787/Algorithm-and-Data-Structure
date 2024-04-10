from collections import deque
stack = deque()

stack.append('https://www.cnn.com')
stack.append('https://www.cnn.com/world')
stack.append('https://www.cnn.com/india')
stack.append('https://www.cnn.com/china')

print(stack)
stack.pop()
print(stack)




# Below is the code to create an stack with list. The issue is when we use dynamic array for a list
# and add extra data Python creates a new memory space and copy all previous data into it.
# # So we use deque
# s = []
#
# s.append('https://www.cnn.com')
# s.append('https://www.cnn.com/world')
# s.append('https://www.cnn.com/india')
# s.append('https://www.cnn.com/china')
#
# print(s[-1])
