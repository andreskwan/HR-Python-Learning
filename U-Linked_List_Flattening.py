class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head: Node = None, init_list=None):
        self.head = head
        self.tail = self.head
        self.length = 0
        if init_list:
            for value in init_list:
                self.append_value(value)

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

    def append_value(self, value):
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

    def append(self, node: Node):
        """ Append a value to the end of the list. """
        self.length += 1
        # print("id(node):" + str(id(node)) + " - node.value: " + str(node.value))
        if self.head is None:
            self.head = node
            self.tail = self.head
            return
        if self.tail:
            self.tail.next = node
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
            self.append_value(value)
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

    def is_circular(self):
        fast = self.head
        slow = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


def merge(list1, list2):
    list1.tail.next = list2.head
    list1.tail = list2.tail
    return list1


class NestedLinkedList(LinkedList):
    def flatten(self):
        """

        :rtype: LinkedList
        """
        # TODO: Implement this method to flatten the linked list in ascending sorted order.
        pass


# First Test scenario
linked_list = LinkedList(head=Node(1))
linked_list.append_value(3)
linked_list.append_value(5)
# linked_list.append_value(Node(3))
# linked_list.append_value(Node(5))
print(linked_list.to_list())

linked_list2 = LinkedList(head=Node(7))
linked_list2.append(Node(9))
linked_list2.append(Node(8))
# linked_list2.append_value(4)
# linked_list2.append_value(8)

linkedList3 = merge(linked_list, linked_list2)
print(linkedList3.to_list())

# # nested_linked_list = NestedLinkedList(Node(linked_list))
#
# second_linked_list = LinkedList(Node(2))
# second_linked_list.append_value(4)
#
# nested_linked_list.append_value(Node(second_linked_list))
#
# solution = nested_linked_list.flatten()
# assert solution == [1,2,3,4,5]
