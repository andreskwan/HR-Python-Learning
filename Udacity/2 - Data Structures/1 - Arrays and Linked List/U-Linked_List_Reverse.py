class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None, tail=None, length=0):
        self.head = head
        self.tail = tail
        self.length = length

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
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return
        if self.tail:
            self.tail.next = Node(value)
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


def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    _array = linked_list.to_list()
    length = linked_list.length
    new_list = []
    # _array = [1, 2, 3, 4, 5, 6, 7, 8]
    # length = len(_array)
    for down_index in range(length - 1, -1, -1):
        # # print(i)
        # up_index = (length - 1) - down_index
        # # print(up_index)
        value = _array[down_index]
        # print(value)
        new_list.append(value)
    return create_linked_list_better(new_list)


def create_linked_list_better(input_list):
    head2 = None
    tail = None
    i = 0
    if 0 < len(input_list):
        i = 1
        head2 = Node(input_list[0])
    else:
        return head2

    tail = head2

    while i < len(input_list):
        tail.next = Node(input_list[i])
        # update tail
        tail = tail.next
        i += 1
    tail.next = None
    return LinkedList(head2, tail, len(input_list))


def reverse_udacity(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """

    new_list = LinkedList()
    node = linked_list.head
    prev_node = None

    # A bit of a complex operation here. We want to take the
    # node from the original linked list and prepend it to
    # the new linked list
    for value in linked_list:
        new_node = Node(value)
        new_node.next = prev_node
        prev_node = new_node
    new_list.head = prev_node
    return new_list


original_list = LinkedList()
for value in [4, 2, 5, 1, -3, 0]:
    original_list.append(value)

flipped = reverse(original_list)
is_correct = list(flipped) == list([0, -3, 1, 5, 2, 4]) and list(original_list) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")
