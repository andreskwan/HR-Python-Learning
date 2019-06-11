class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        self.tail = self.head
        self.length = 0
        if init_list:
            for value in init_list:
                self.append(value)

    def __iter__(self):
        """
        https://rszalski.github.io/magicmethods/

        if you want your object to be iterable, you'll have to define __iter__,
        which returns an iterator.
        That iterator must conform to an iterator protocol,
        which requires iterators to have methods called
        __iter__(returning itself) and next

        :return: yield node.value
        """
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        """
        It's often useful to have a string representation of a class.
        Defines behavior for when repr() is called on an instance of your class. The major difference between str() and
        repr() is intended audience. repr() is intended to produce output that is mostly machine-readable (in many cases,
         it could be valid Python code even), whereas str() is intended to be human-readable.
        :return:
        """
        return str([v for v in self])

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        self.length += 1
        if self.head:
            temporal = self.head
            self.head = Node(value)
            self.head.next = temporal
            return
        self.head = Node(value)
        self.tail = self.head

    def append(self, value):
        """ Append a value to the end of the list. """
        self.length += 1
        new_node = Node(value)
        # print("id(node):" + str(id(new_node)) + " - node.value: " + str(new_node.value))
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return
        if self.tail:
            self.tail.next = new_node
            self.tail = self.tail.next

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        current_node = self.head
        while current_node:  #
            if current_node.value == value:
                return current_node
            current_node = current_node.next  # update current_node
        return None

    def remove(self, value):
        """ Remove first occurrence of value. """
        # find the node
        # if not found - None
        # if found
        # - I need to know
        # the previous node
        # - because I need to append the next node of the node is going to be removed to it
        current_node = self.head
        while current_node:  #
            if current_node.value == value:
                new_head = current_node.next
                self.head = new_head
                self.length -= 1
                return
            if current_node.next.value == value:
                self.length -= 1
                temporal = current_node.next.next  # preserve the rest of the list
                current_node.next = temporal
                if current_node.next is None:
                    self.tail = current_node
                return
            current_node = current_node.next
        return None

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        if self.head is None:
            return None
        actual_value = self.head.value
        self.remove(actual_value)
        return actual_value

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        if pos == 0:
            self.prepend(value)
            return
        if self.length < pos:
            self.append(value)
            return
        current_node = self.head
        position = 1
        while current_node.next:
            if position == pos:
                temporal = current_node.next
                new_node = Node(value)
                new_node.next = temporal
                current_node.next = new_node
                self.length += 1
                return
            position += 1
            current_node = current_node.next

    def size(self):
        """ Return the size or length of the linked list. """
        return self.length

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


# Mistake
# def is_circular(linked_list):
#     current_node = linked_list.head
#
#     while current_node:
#         if current_node.next.next or current_node.next is None:
#             return False
#         fast = id(current_node.next.next)
#         print("fast: " )
#         slow = id(current_node.next)
#         current_node = current_node.next
#         if fast == slow:
#             print("fast " + str(fast) + " slow " + str(slow))
#             return True
#     return False


def is_circular(linked_list):
    """
    Determine weather the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise

    fast pointer two nodes per step
       -- how? node.next.next
    slow pointer one node per step
       -- how? node.next

    how do they know they are pointing to the same node,
    by comparing their memory address.
    """
    fast = linked_list.head
    slow = linked_list.head

    while fast and fast.next:
        # if fast.next.next is None or fast.next is None:
            # return False
        # fast = id(fast.next.next)
        fast = fast.next.next
        print("fast: " )
        # slow = id(fast.next)
        slow = slow.next  # this is the key

        print("fast " + str(fast) + " slow " + str(slow))
        print("fast id: " + str(id(fast)) + " slow id: " + str(id(slow)))
        print("fast value " + str(fast.value) + " slow value " + str(slow.value))
        if fast == slow:
            print("fast " + str(fast) + " slow " + str(slow))
            print("is circular")
            print("--------")
            return True
    print("fast " + str(fast) + " slow " + str(slow))
    print("fast id: " + str(id(fast)) + " slow id: " + str(id(slow)))
    # print("fast value " + str(fast.value) + " slow value " + str(slow.value))
    print("--------")
    return False


# list_with_loop = LinkedList([2, -1, 3, 0, 5])
list_with_loop = LinkedList([4, 4, 4, 4, 4])

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next:
    node = node.next
node.next = loop_start


small_loop = LinkedList([0])
small_loop.head.next = small_loop.head
print("Pass" if is_circular(list_with_loop) else "Fail")

print("Pass" if not is_circular(LinkedList([-4, 7, 2, 5, -1])) else "Fail")
# print("--------")
print("Pass" if not is_circular(LinkedList([4, 4, 4, 4, 4])) else "Fail")
# print("--------")
print("Pass" if not is_circular(LinkedList([1])) else "Fail")
# print("--------")
print("Pass" if is_circular(small_loop) else "Fail")
# print("--------")
print("Pass" if not is_circular(LinkedList([])) else "Fail")