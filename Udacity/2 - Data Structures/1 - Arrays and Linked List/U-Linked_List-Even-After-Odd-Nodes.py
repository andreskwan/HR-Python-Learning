
import random


class Node:
    def __init__(self, value):
        # if value is None:
        #     return None
        self.value = value
        self.next = None


class LinkedList(Node):
    def __init__(self, head: Node = None, init_list=None):
        self.head = head
        self.tail = self.head
        self.length = 0

        if init_list:
            for value in init_list:
                self.append_value(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
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

    def remove_first_occurrence(self, value):
        if value == self.head.value and self.size() == 1:
            self.length = 0
            self.head = None
            self.tail = None
            return
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
        """ Return the first node's value and remove_first_occurrence it from the list. """
        if self.head is None:
            return None
        actual_value = self.head.value
        self.remove_first_occurrence(actual_value)
        return actual_value

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        if pos == 0:
            self.prepend(value)
            return
        if self.size() < pos:
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
        current = self.head
        count = 0
        # TODO: fix self.length, it should be updated to avoid O(n) and return to O(1)
        while current:
            count += 1
            current = current.next
        self.length = count
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


def swap_nodes(node_n, node_a, node_b):
    if node_n is None or node_a is None or node_b is None:
        return None
    node_n.next = node_b
    node_a.next = node_b.next
    node_b.next = node_a


def swap_data(node_a, node_b):
    if node_a is None or node_b is None:
        return None
    temp = node_a.value
    node_a.value = node_b.value
    node_b.value = temp


def insert_node_after(actual_node, new_value):
    temp = actual_node.next
    second_node = Node(new_value)
    second_node.next = temp
    actual_node.next = second_node


def sort(unsorted_list):
    if 0 == unsorted_list.length:
        return None
    if 1 == unsorted_list.length:
        return unsorted_list
    first = unsorted_list.pop()
    # second = unsorted_list.pop()
    sorted_list = LinkedList(Node(first))

    while unsorted_list.length > 0:  # if there is more to sort
        current = sorted_list.head
        value = unsorted_list.pop()  # get head from unsorted
        previous = current
        if value < current.value:
            sorted_list.prepend(value)
            continue
        while current.value < value and current.next is not None:
            previous = current
            current = current.next
        if previous.next is None:
            sorted_list.append_value(value)
        else:
            if current.value < value and current.next is None:
                sorted_list.append_value(value)
            else:
                insert_node_after(previous, value)
    return sorted_list


def merge(list1, list2):
    if list1 is None and list2 is None:
        return None
    if list1 is None:
        return sort(list2)
    if list2 is None:
        return sort(list1)
    if list1.length == 0 and list2.length == 0:
        return None
    if list1.length is not 0:
        list1.tail.next = list2.head
        list1.tail = list2.tail
        return sort(list1)
    else:
        return sort(list2)