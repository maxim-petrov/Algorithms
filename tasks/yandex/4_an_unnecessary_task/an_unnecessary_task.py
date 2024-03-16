class Stack:

    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[-1]

    def size(self):
        return len(self.__items)


stack = Stack()
stack.push('Gusev')
stack.push('Gale')
stack.push('Elysium')
stack.push('Jezero')
stack.push('Meridiani')
print(stack.pop())