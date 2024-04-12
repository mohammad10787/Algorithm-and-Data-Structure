from collections import deque
# stack = deque()
#
# stack.append('https://www.cnn.com')
# stack.append('https://www.cnn.com/world')
# stack.append('https://www.cnn.com/india')
# stack.append('https://www.cnn.com/china')
#
# print(stack)
# stack.pop()
# print(stack)




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

# Stack Excersise

#reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def reverse_string(self, string):
        a = ""
        for char in string:
            self.push(char)
        while self.size() != 0:
            a += str(self.pop())
        return(a)

    def is_match(self, ch1, ch2):
        match_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        return match_dict[ch1] == ch2

    def is_balanced(self, string):
        for ch in string:
            if ch == '(' or ch == '{' or ch == '[':
                self.push(ch)
            if ch == ')' or ch == '}' or ch == ']':
                if self.size() == 0:
                    return False
                if not self.is_match(ch, self.pop()):
                    return False

        return self.size() == 0


if __name__ == "__main__":
    s = Stack()
    # print(s.reverse_string("We will conquere COVID-19"))
    print(s.is_balanced("({a+b})"))
    print(s.is_balanced("))((a+b}{"))
    print(s.is_balanced("((a+b))"))
    print(s.is_balanced("))"))
    print(s.is_balanced("[a+b]*(x+2y)*{gg+kk}"))

# 2-Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class
# from the tutorial.