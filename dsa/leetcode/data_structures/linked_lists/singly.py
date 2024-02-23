# structure of a linked list, 10 --> 5 --> 16
# linked_list = {
#     'head': {
#         'value': 10,
#         'next': {
#             'value': 5,
#             'next': {
#                 'value': 16,
#                 'next': None
#             }
#         },
#     }
# }


# node class holds a value and reference
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# LinkedList using a Node class
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1


    def append(self, value):
        new_node = Node(value)

        self.tail.next = new_node
        self.tail = new_node
        
        self.length += 1
        return self


    def prepend(self, value):
        new_node = Node(value)

        new_node.next = self.head
        self.head = new_node
        
        self.length += 1
        return self


    def insert(self, index, value):
        new_node = Node(value)
        next_node = self.traverse(index-1)

        new_node.next = next_node.next
        next_node.next = new_node
        
        self.length += 1
        return self


    def remove(self, index):
        next_node = self.traverse(index-1)

        if index == 0:
            self.head = next_node.next
        
        elif index == self.length - 1:
            next_node.next = None
            self.tail = next_node
        
        else:
            next_node.next = next_node.next.next
        
        self.length -= 1
        return self
    

    def traverse(self, index):
        if index == -1:
            return self.head
        
        elif index == self.length - 1:
            return self.tail

        elif index < 0:
            print(f"Error: Invalid index {index}.")
            exit()

        elif index == self.length:
            print(f"Error: End of LinkedList of size {self.length} reached.")
            exit()
        
        next_node = self.head

        for _ in range(index):
            next_node = next_node.next

        return next_node
        
    
    def reverse(self):
        """
        Reverses the linked list using a stack.
        """
        nodes = []
        for _ in range(self.length):
            nodes.append(self.traverse(_))

        node = nodes.pop()
        self.head = node
        while len(nodes) != 0:
            next_node = nodes.pop()
            node.next = next_node
            node = next_node

            if len(nodes) == 0:
                node.next = None
                self.tail = node
                break

        return self

    def to_string(self):
        next_node = self.head
        for _ in range(self.length):
            print(next_node.value, end=" ")
            next_node = next_node.next

        print("\n")

# LinkedList with the Node as a dict
# This is easier to read but code is duplicated and to get the head or next requires dict syntax.
# e.g. self.head['next'] = new_node
# If a node class is used instead, see `LinkedList` above, then dot syntax can be used.
# e.g. self.head.next = new_node
class LinkedListNodeDict:
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None
        }

        self.tail = self.head
        self.length = 1


    def append(self, value):
        new_node = {
            'value': value,
            'next': None
        }

        self.tail['next'] = new_node
        self.tail = new_node

        self.length += 1

        return self


    def prepend(self, value):
        new_node = {
            'value': value,
            'next': None
        }

        new_node['next'] = self.head
        self.head = new_node

        self.length += 1

        return self


def main():
    # 10 --> 5
    linked_list = LinkedList(10)
    linked_list.append(5)
    print("append", 5)
    print("head:", linked_list.head.value)
    print("tail:", linked_list.tail.value)
    linked_list.to_string()

    # 10 --> 5 --> 16
    linked_list.append(16)
    print("append", 16)
    print("head:", linked_list.head.value)
    print("tail:", linked_list.tail.value)
    linked_list.to_string()


    # 1 --> 10 --> 5 --> 16
    linked_list.prepend(1)
    print("prepend", 1)
    print("head:", linked_list.head.value)
    print("tail:", linked_list.tail.value)
    linked_list.to_string()


    # 1 --> 10 --> 99 --> 5 --> 16
    linked_list.insert(2, 99)
    print(f"insert {99} at {2}")
    print("head:", linked_list.head.value)
    print("tail:", linked_list.tail.value)
    linked_list.to_string()

    # 16 --> 5 --> 99 --> 10 --> 1
    linked_list.reverse().to_string()

    # 16 --> 5 --> 99 --> 1
    linked_list.remove(3)
    print("remove", 3)
    print("head:", linked_list.head.value)
    print("tail:", linked_list.tail.value)
    linked_list.to_string()

    # 16 --> 5 --> 99
    linked_list.remove(3)
    print("remove", 3)
    print("head:", linked_list.head.value)
    print("tail:", linked_list.tail.value)
    linked_list.to_string()

    # 5 --> 99
    linked_list.remove(0)
    print("remove", 0)
    print("head:", linked_list.head.value)
    print("tail:", linked_list.tail.value)
    linked_list.to_string()

    # 5
    linked_list.remove(1)
    print("remove", 1)
    print("head:", linked_list.head.value)
    print("tail:", linked_list.tail.value)
    linked_list.to_string()
    

if __name__ == "__main__":
    main()