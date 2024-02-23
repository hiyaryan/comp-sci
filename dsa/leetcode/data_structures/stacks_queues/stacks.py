# Stacks LIFO--Last in, First Out
# The last item that comes in is the first item that comes out

# methods: lookup O(n), pop O(1), push O(1), peek O(1)

# consider using an array for a stack if memory is fixed
#     - if an array is allocated a space of 50 and a new item is pushed onto
#       it, the entire  array needs to be copied into a new memory location
#       just to add. Arrays are stored in contiguous spaces of memory
#
# consider using a linked list for a stack if memory is dynamic
#     - items in a linked list are not stored in contiguous slots of memory,
#       they simply reference the next item, so no copying needs to be done to
#       add an item to the list, it can just keep growing


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, node=None):
        self.top = node
        self.bottom = node
        self.length = 0

    def peek(self):
        if self.is_empty():
            print("Stack is empty.\n")

        else:
            print(f"{self.length}: {self.top.value}\n")

    def push(self, value):
        """
        Add a node to the top of the stack.
        """
        new_node = Node(value)

        if self.is_empty():
            self.top = new_node
            self.bottom = new_node

        else:
            new_node.next = self.top
            self.top = new_node

        self.length += 1

    def pop(self):
        if self.is_empty():
            print("Nothing to pop from stack.\n")

        else:
            popped_value = self.top.value
            self.top = self.top.next
            self.length -= 1

            if self.length == 0:
                self.bottom = None

            return popped_value

    def is_empty(self):
        return True if self.length == 0 else False


class ArrayStack:
    def __init__(self, value=[]):
        self.stack = value

    def peek(self):
        if self.is_empty():
            print("Stack is empty.\n")

        else:
            print(f"{len(self.stack)}: {self.stack[len(self.stack) - 1]}\n")

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            print("Nothing to pop from stack.\n")

        else:
            return self.stack.pop()

    def is_empty(self):
        return True if len(self.stack) == 0 else False


def main():
    # Stack as a Linked List
    print("COMMAND: new stack.")
    stack = Stack()
    print(stack.bottom, end="\n\n")

    print("COMMAND: is empty")
    print(stack.is_empty(), end="\n\n")

    print("COMMAND: peek")
    stack.peek()

    print("COMMAND: pop")
    stack.pop()

    print("COMMAND: push google && peek")
    stack.push("google")
    stack.peek()

    print("COMMAND: push Udemy && peek")
    stack.push("Udemy")
    stack.peek()

    print("COMMAND: push Discord && peek")
    stack.push("Discord")
    stack.peek()

    print("COMMAND: is empty")
    print(stack.is_empty(), end="\n\n")

    print("COMMAND: pop")
    print(stack.pop())
    stack.peek()

    print("COMMAND: pop")
    print(stack.pop())
    stack.peek()

    print("COMMAND: pop")
    print(stack.pop())
    stack.peek()

    print("COMMAND: pop")
    stack.pop()

    print("COMMAND: peek")
    stack.peek()

    print("COMMAND: is empty")
    print(stack.is_empty(), end="\n\n")

    # Stack as a list (or array)
    print("COMMAND: new array_stack.")
    array_stack = ArrayStack()
    print(array_stack.stack, end="\n\n")

    print("COMMAND: is empty")
    print(array_stack.is_empty(), end="\n\n")

    print("COMMAND: peek")
    array_stack.peek()

    print("COMMAND: pop")
    array_stack.pop()

    print("COMMAND: push google && peek")
    array_stack.push("google")
    array_stack.peek()

    print("COMMAND: push Udemy && peek")
    array_stack.push("Udemy")
    array_stack.peek()

    print("COMMAND: push Discord && peek")
    array_stack.push("Discord")
    array_stack.peek()

    print("COMMAND: is empty")
    print(array_stack.is_empty(), end="\n\n")

    print("COMMAND: pop")
    print(array_stack.pop())
    array_stack.peek()

    print("COMMAND: pop")
    print(array_stack.pop())
    array_stack.peek()

    print("COMMAND: pop")
    print(array_stack.pop())
    array_stack.peek()

    print("COMMAND: pop")
    array_stack.pop()

    print("COMMAND: peek")
    array_stack.peek()

    print("COMMAND: is empty")
    print(array_stack.is_empty(), end="\n\n")


if __name__ == "__main__":
    main()
