# Queues FIFO--first in, first out
# the first item that comes in in the first item that comes out

# methods: lookup O(n), enqueue O(1), dequeue O(1), peek O(1)


# never build a queue with an array
#    - Arrays contain indices, that must be shifted anytime an item is dequeued
#      from the list


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, node=None):
        self.first = node
        self.last = node
        self.length = 0

    def peek(self):
        if self.is_empty():
            print("Queue is empty.\n")

        else:
            print(f"Next: {self.first.value}\n")

    def enqueue(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.first = new_node
            self.last = new_node

        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1

    def dequeue(self):
        if self.is_empty():
            print("Nothing to dequeue.\n")

        else:
            dequeued = self.first.value
            self.first = self.first.next

            self.length -= 1

            if self.is_empty:
                self.last = None

            return dequeued

    def is_empty(self):
        return True if self.length == 0 else False


def main():
    print("COMMAND: create queue")
    queue = Queue()
    print(f"{queue.first}", end="\n\n")

    print("COMMAND: is empty")
    print(queue.is_empty(), end="\n\n")

    print("COMMAND: peek")
    queue.peek()

    print("COMMAND: dequeue")
    queue.dequeue()

    print("COMMAND: enqueue Joy && peek")
    queue.enqueue("Joy")
    queue.peek()

    print("COMMAND: enqueue Matt && peek")
    queue.enqueue("Matt")
    queue.peek()

    print("COMMAND: enqueue Pavel && peek")
    queue.enqueue("Pavel")
    queue.peek()

    print("COMMAND: enqueue Samir && peek")
    queue.enqueue("Samir")
    queue.peek()

    print("COMMAND: is empty")
    print(queue.is_empty(), end="\n\n")

    print("COMMAND: dequeue && peek")
    print(queue.dequeue())
    queue.peek()

    print("COMMAND: dequeue && peek")
    print(queue.dequeue())
    queue.peek()

    print("COMMAND: dequeue && peek")
    print(queue.dequeue())
    queue.peek()

    print("COMMAND: dequeue && peek")
    print(queue.dequeue())
    queue.peek()

    print("COMMAND: dequeue")
    queue.dequeue()

    print("COMMAND: peek")
    queue.peek()

    print("COMMAND: is empty")
    print(queue.is_empty(), end="\n\n")


if __name__ == "__main__":
    main()
