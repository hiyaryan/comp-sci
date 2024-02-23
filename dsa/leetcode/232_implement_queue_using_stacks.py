# 232. Implement Queue using Stacks
# ref. https://leetcode.com/problems/implement-queue-using-stacks/description/
# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:
#     void push(int x) Pushes element x to the back of the queue.
#     int pop() Removes the element from the front of the queue and returns it.
#     int peek() Returns the element at the front of the queue.
#     boolean empty() Returns true if the queue is empty, false otherwise.

# Notes:
#   You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
#   Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

# Example 1:

# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]

# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false

# Constraints:
#     1 <= x <= 9
#     At most 100 calls will be made to push, pop, peek, and empty.
#     All the calls to pop and peek are valid.

# Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.


class MyQueue(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        else:
            # get the stack reversed
            rarr = self.reverse(self.stack)

            # pop the next item from the reversed stack
            item = rarr.pop()

            # re-reverse the reversed stack and set this stack to it
            self.stack = self.reverse(rarr)

            return item

    def peek(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        else:
            return self.stack[0]

    def empty(self):
        """
        :rtype: bool
        """
        return True if len(self.stack) == 0 else False

    @staticmethod
    def reverse(arr):
        rarr = []

        for item in range(len(arr))[::-1]:
            rarr.append(arr[item])

        return rarr


def main():
    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    x = 4
    print(f"COMMAND push {x}\n")
    obj.push(x)

    x = 3
    print(f"COMMAND push {x}\n")
    obj.push(x)

    x = 5
    print(f"COMMAND push {x}\n")
    obj.push(x)

    x = 6
    print(f"COMMAND push {x}\n")
    obj.push(x)

    print(f"STACK: {obj.stack}\n")
    print(f"COMMAND: pop {obj.pop()}\n")
    print(f"COMMAND: peek {obj.peek()}\n")
    print(f"COMMAND: empty {obj.empty()}\n")

    print(f"STACK: {obj.stack}\n")
    print(f"COMMAND: pop {obj.pop()}\n")
    print(f"COMMAND: peek {obj.peek()}\n")

    x = 8
    print(f"COMMAND push {x}\n")
    obj.push(x)

    x = 9
    print(f"COMMAND push {x}\n")
    obj.push(x)

    print(f"COMMAND: peek {obj.peek()}\n")

    print(f"STACK: {obj.stack}\n")
    print(f"COMMAND: pop {obj.pop()}\n")
    print(f"COMMAND: peek {obj.peek()}\n")

    print(f"STACK: {obj.stack}\n")
    print(f"COMMAND: pop {obj.pop()}\n")
    print(f"COMMAND: peek {obj.peek()}\n")

    print(f"STACK: {obj.stack}\n")
    print(f"COMMAND: pop {obj.pop()}\n")
    print(f"COMMAND: peek {obj.peek()}\n")

    print(f"STACK: {obj.stack}\n")
    print(f"COMMAND: pop {obj.pop()}\n")
    print(f"COMMAND: peek {obj.peek()}\n")
    print(f"COMMAND: empty {obj.empty()}\n")

    print(f"STACK: {obj.stack}\n")
    print(f"COMMAND: pop {obj.pop()}\n")
    print(f"COMMAND: peek {obj.peek()}\n")
    print(f"COMMAND: empty {obj.empty()}\n")


if __name__ == "__main__":
    main()
