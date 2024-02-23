# Doubly Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, value=None):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 0 if not value else 1

    def prepend(self, value):
        """
        Add new value to the head of the list
        """
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return
        
        new_node.next = self.head
        self.head.prev = new_node

        self.head = new_node
        self.length += 1


    def append(self, value):
        """
        Add new value to tail of list.
        """
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node

        self.tail = new_node
        self.length += 1

    def lookup_from_head(self, index):
        """
        Traverse the list from the head and return the node at the given index.
        """
        if index < 0 or index > self.length:
            raise IndexError(f"Index {index} is invalid.")

        next_node = self.head
        for _ in range(index):
            next_node = next_node.next

        return next_node
        

    def lookup_from_tail(self, index):
        """
        Traverse the list from the tail and return the node at the given index.
        """
        if index < 0 or index > self.length:
            raise IndexError(f"Index {index} is invalid.")

        next_node = self.tail
        for _ in range(self.length - index - 1):
            next_node = next_node.prev

        return next_node
    

    def insert(self, traversal, index, value):
        """
        Insert a new value into the list with a traversal function.
        """
        if index == 0:
            self.prepend(value)
            return
        
        if index == self.length - 1:
            self.append(value)
            return

        new_node = Node(value)        
        next_node = traversal(index)

        new_node.prev = next_node.prev
        new_node.next = next_node

        next_node.prev.next = new_node
        next_node.prev = new_node

        self.length += 1
        

    def delete(self, traversal, index):
        """
        Delete by index with a traversal function.
        """
        next_node = traversal(index)

        if index == 0:
            next_node.next.prev = None
            self.head = next_node.next
        elif index == self.length - 1:
            next_node.prev.next = None
            self.tail = next_node.prev
        else:
            next_node.prev.next = next_node.next
            next_node.next.prev = next_node.prev

        self.length -= 1


    def print_from_head(self):
        print("LIST", end=" ")

        next_node = self.head
        for _  in range(self.length):
            print(next_node.value, end=" ")
            next_node = next_node.next

        print("\n")



def main():
    # initialize an empty double linked list
    dll = DoublyLinkedList()
    print("COMMAND: create double linked list")
    print("head:", dll.head.value)
    print("tail:", dll.tail.value)
    dll.print_from_head()

    print("COMMAND: append 5")
    dll.append(5)
    print("head:", dll.head.value)
    print("tail:", dll.tail.value)
    dll.print_from_head()

    print("COMMAND: append 9")
    dll.append(9)
    print("head:", dll.head.value)
    print("tail:", dll.tail.value)
    dll.print_from_head()

    print("COMMAND: append 7")
    dll.append(7)
    print("head:", dll.head.value)
    print("tail:", dll.tail.value)
    dll.print_from_head()

    print("COMMAND: prepend 11")
    dll.prepend(11)
    print("head:", dll.head.value)
    print("tail:", dll.tail.value)
    dll.print_from_head()

    print("COMMAND: prepend 2")
    dll.prepend(2)
    print("head:", dll.head.value)
    print("tail:", dll.tail.value)
    dll.print_from_head()

    print("COMMAND: insert 13 at 3, traverse from head")
    dll.insert(lambda index: dll.lookup_from_head(index), 3, 13)
    print("head:", dll.head.value)
    print("tail:", dll.tail.value)
    dll.print_from_head()

    print("COMMAND: insert 17 at 4, traverse from tail")
    dll.insert(lambda index: dll.lookup_from_tail(index), 4, 17)
    print("head:", dll.head.value)
    print("tail:", dll.tail.value)
    dll.print_from_head()

    print("COMMAND: delete at 5, traverse from tail")
    dll.delete(lambda index: dll.lookup_from_tail(index), 5)
    print("head:", dll.head.value)
    print("tail:", dll.tail.value)
    dll.print_from_head()

    print("COMMAND: delete at 5, traverse from tail")
    dll.delete(lambda index: dll.lookup_from_tail(index), 5)
    print("head:", dll.head.value)
    print("tail:", dll.tail.value)
    dll.print_from_head()

    print("COMMAND: delete at 0, traverse from head")
    dll.delete(lambda index: dll.lookup_from_head(index), 0)
    print("head:", dll.head.value)
    print("tail:", dll.tail.value)
    dll.print_from_head()

    print("COMMAND: insert 29 at 0, traverse from head")
    dll.insert(lambda index: dll.lookup_from_head(index), 0, 29)
    print("head:", dll.head.value)
    print("tail:", dll.tail.value)
    dll.print_from_head()    

    # print("COMMAND: insert 100 at -1, traverse from head")
    # dll.insert(lambda index: dll.lookup_from_head(index), -1, 100)
    # print("head:", dll.head.value)
    # print("tail:", dll.tail.value)
    # dll.print_from_head()   

if __name__ == "__main__":
    main()