class Stack:
    # constructor
    def __init__(self):
        self.__stack = []  # create private stack

    # methods
    def pop(self):  # pop the item
        if self.isEmpty():
            return None
        return self.__stack.pop()

    def peek(self):  # peek the item (no removal)
        if self.isEmpty():
            return None
        return self.__stack[len(self.__stack) - 1]

    def push(self, item):  # push the item
        self.__stack.append(item)

    def getSize(self):  # return stack size
        return len(self.__stack)

    def isEmpty(self):  # check if stack empty
        return self.getSize() == 0

    def __str__(self):  # display the stack in reverse order
        result = ""
        for i, item in enumerate(reversed(self.__stack)):
            result += f"{i}\t{self.__stack[i]}\n"
        return result

    def swap(self):  # swap the top with top-1 item
        if self.getSize() < 2:
            return
        top = self.pop()
        top_minus_1 = self.pop()
        self.push(top)
        self.push(top_minus_1)

    def copy(self):  # duplicate the top item
        top = self.peek()
        if top is not None:
            self.push(top)

    def flush(self):  # empty the stack
        self.__stack = []


def main():
    mystack = Stack()
    for i in range(1, 4):
        mystack.push(i * 10)

    print("test __str__")
    print(mystack)

    print("test swap")
    mystack.swap()
    print(mystack)

    print("test copy")
    mystack.copy()
    print(mystack)

    print("test flush")
    mystack.flush()
    mystack.push(11)
    print(mystack)


# call the main function if this file is directly executed
if __name__ == "__main__":
    main()
    
