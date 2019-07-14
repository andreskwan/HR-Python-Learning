import random


class Node:
    def __init__(self, value):
        # if value is None:
        #     return None
        self.value = value
        self.next = None


class LinkedList(Node):
    def __init__(self, head: Node = None, init_list=None):
        # if head is None:
        #     if len(init_list) is 0:
        #         return None
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
        """ Remove first occurrence of value.
        find the node
        if not found - None
        if found
        - I need to know
        the previous node
        - because I need to append the next node of the node is going to be removed to it
        """
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
        self.remove(actual_value)
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
    """
    n->a->b->c expected n->b->a->c
    :param node_n: previous node
    :param node_a: actual node
    :param node_b: next node
    :return:
    """
    if node_n is None or node_a is None or node_b is None:
        return None
    node_n.next = node_b
    node_a.next = node_b.next
    node_b.next = node_a


def test_swap_nodes():
    print("--------------------------")
    print("-------test_swap_nodes-------")
    test_cases = [
        ([1, 3, 2, 4], [1, 2, 3, 4])]

    for (args, answer) in test_cases:
        print("---------------------")
        result = LinkedList(init_list=args)
        swap_nodes(result.head, result.head.next, result.head.next.next)

        temporal_answer = LinkedList(init_list=answer)
        if result is not None and temporal_answer is not None:
            print("input:    " + str(args) + " |\nexpected: " + str(temporal_answer.to_list()) + " |\nresult:   " + str(
                result.to_list()))
            if result.to_list() == temporal_answer.to_list():
                print("Test case passed!")
            else:
                print("**********************Test with input data:", args, "failed")
        else:
            print("result: " + str(result) + " |\nexpected: " + str(answer))
            if result == answer:
                print("Test case passed!")
            else:
                print("**********************Test with input data:", args, "failed")


test_swap_nodes()


def swap_data(node_a, node_b):
    """
    n(1)->a(3)->b(2)->c expected n(1)->a(2)->b(3)->c
    :param node_a: actual node
    :param node_b: next node
    :return:
    """
    if node_a is None or node_b is None:
        return None
    temp = node_a.value
    node_a.value = node_b.value
    node_b.value = temp


def test_swap_data():
    print("--------------------------")
    print("-------test_swap_data-------")
    test_cases = [
        ([1, 3, 2, 4], [1, 2, 3, 4])]

    for (args, answer) in test_cases:
        print("---------------------")
        result = LinkedList(init_list=args)
        swap_data(result.head.next, result.head.next.next)

        temporal_answer = LinkedList(init_list=answer)
        if result is not None and temporal_answer is not None:
            print("input:    " + str(args) + " |\nexpected: " + str(temporal_answer.to_list()) + " |\nresult:   " + str(
                result.to_list()))
            if result.to_list() == temporal_answer.to_list():
                print("Test case passed!")
            else:
                print("**********************Test with input data:", args, "failed")
        else:
            print("result: " + str(result) + " |\nexpected: " + str(answer))
            if result == answer:
                print("Test case passed!")
            else:
                print("**********************Test with input data:", args, "failed")


# test_swap_data()


def insert_node_after(actual_node, new_value):
    """

    :param actual_node:
    :param new_value:
    :return:
    """
    temp = actual_node.next
    second_node = Node(new_value)
    second_node.next = temp
    actual_node.next = second_node


def test_insert_node_after():
    print("--------------------------")
    print("-------test_insert_node_after-------")
    #  input (), output ()
    # ([], None),
    test_cases = [
        (([1, 3, 4], 2), [1, 2, 3, 4])]

    for (args, answer) in test_cases:
        print("---------------------")
        args_list = args[0]
        arg_value = args[1]
        result = LinkedList(init_list=args_list)
        insert_node_after(result.head, arg_value)

        temporal_answer = LinkedList(init_list=answer)
        if result is not None and temporal_answer is not None:
            print("input:    " + str(args) + " |\nexpected: " + str(temporal_answer.to_list()) + " |\nresult:   " + str(
                result.to_list()))
            if result.to_list() == temporal_answer.to_list():
                print("Test case passed!")
            else:
                print("**********************Test with input data:", args, "failed")
        else:
            print("result: " + str(result) + " |\nexpected: " + str(answer))
            if result == answer:
                print("Test case passed!")
            else:
                print("**********************Test with input data:", args, "failed")


# test_insert_node_after()


def test_pop():
    print("--------------------------")
    print("-------test_pop-------")
    test_cases = [([], (None, None)),
                  ([1], (1, None)),
                  ([1, 2], (1, [2])),
                  ([2, 1], (2, [1])),
                  ([2, 1, 3], (2, [1, 3]))]

    for (args, answer) in test_cases:
        print("---------------------")
        temporal_list = LinkedList(init_list=args)
        print("temporal_list: " + str(temporal_list.to_list()))
        pop_value = temporal_list.pop()
        value_answer = answer[0]
        temporal_answer = LinkedList(init_list=answer[1])
        if pop_value is not None and value_answer is not None:
            # print("temporal_list: "+str(temporal_list.to_list()) + " and temporal_answer: "+str(temporal_answer.to_list()))
            print("pop_value: " + str(pop_value) + " |\nexpected: " + str(answer[0]))
            if temporal_answer.to_list() == temporal_answer.to_list():
                print("Test case passed!")
            else:
                print("**********************Test with input data:", args, "failed")
        else:
            print("pop_value: " + str(pop_value) + " |\nexpected: " + str(answer[0]))
            if pop_value == answer[1]:
                print("Test case passed!")
            else:
                print("**********************Test with input data:", args, "failed")


# test_pop()


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
        # TODO: how to split in a half the sorted_list
        # so I could inser faster a new value?
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


def test_sort():
    print("--------------------------")
    print("-------test_sort-------")
    unsorted_list = [random.randint(1, 100000) for x in range(200)]
    sorted_list = sorted(unsorted_list)
    test_cases = [([], None),
                  ([1], [1]),
                  ([1, 2], [1, 2]),
                  ([2, 1], [1, 2]),
                  ([1, 3, 2], [1, 2, 3]),
                  ([2, 3, 1], [1, 2, 3]),
                  ([3, 2, 1], [1, 2, 3]),
                  ([1, 3, 2, 4], [1, 2, 3, 4]),
                  ([3, 2, 1, 4], [1, 2, 3, 4]),
                  ([3, 2, 4, 1], [1, 2, 3, 4]),
                  ([3, 4, 2, 1], [1, 2, 3, 4]),
                  ([4, 3, 2, 1], [1, 2, 3, 4]),
                  ([1, 80, 2, 3, 4], [1, 2, 3, 4, 80]),
                  ([1, 4, 3, 80, 2], [1, 2, 3, 4, 80]),
                  ([80, 3, 2, 4, 1], [1, 2, 3, 4, 80]),
                  ([4, 80, 3, 2, 1], [1, 2, 3, 4, 80]),
                  (unsorted_list, sorted_list)]

    for (args, answer) in test_cases:
        print("---------------------")
        temporal_list = LinkedList(init_list=args)
        result = sort(temporal_list)
        temporal_answer = LinkedList(init_list=answer)
        if result is not None and temporal_answer is not None:
            print("input:    " + str(args) + " |\nexpected: " + str(temporal_answer.to_list()) + " |\nresult:   " + str(
                result.to_list()))
            if result.to_list() == temporal_answer.to_list():
                print("Test case passed!")
            else:
                print("**********************Test with input data:", args, "failed")
        else:
            print("result: " + str(result) + " |\nexpected: " + str(answer))
            if result == answer:
                print("Test case passed!")
            else:
                print("**********************Test with input data:", args, "failed")


# test_sort()


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


def test_merge():
    print("--------------------------")
    print("-------test_merge-------")
    test_cases = [(([], []), None),
                  (([], [4, 7, 1, 0]), [0, 1, 4, 7]),
                  (([4, 7, 1, 0], []), [0, 1, 4, 7]),
                  (([5, 3, 1], [9, 4, 33]), [1, 3, 4, 5, 9, 33])]

    for (args, answer) in test_cases:
        print("---------------------")
        list1 = LinkedList(init_list=args[0])
        list2 = LinkedList(init_list=args[1])
        result = merge(list1, list2)
        if result is not None and answer is not None:
            print("input:    " + str(args) + " |\nexpected: " + str(answer) + " |\nresult:   " + str(
                result.to_list()))
            if result.to_list() == answer:
                print("Test case passed!")
            else:
                print("**********************Test with input data:", args, "failed")
        else:
            print("result: " + str(result) + " |\nexpected: " + str(answer))
            if result == answer:
                print("Test case passed!")
            else:
                print("**********************Test with input data:", args, "failed")


# test_merge()


# class NestedLinkedList(LinkedList):
#     def flatten(self):
#         # if self.size() is 0:
#         #     return None
#         return merge(self.head.value, self.head.next.value)

class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)

    def _flatten(self, node):
        if node.next is None:
            return merge(node.value, None)
        return merge(node.value, self._flatten(node.next))


def test_flatten():
    print("--------------------------")
    print("-------test_flatten-------")
    test_cases = [
                  (([1], [2]), [1, 2]),
                  (([1, 3, 5], [2, 4]), [1, 2, 3, 4, 5])]
    # (([], [4, 7, 1, 0]), [0, 1, 4, 7]),
    # (([4, 7, 1, 0], []), [0, 1, 4, 7]),
    # (([5, 3, 1], [9, 4, 33]), [1, 3, 4, 5, 9, 33])]

    for (args, answer) in test_cases:
        print("--------------------------")
        # for list in args:
        list1 = LinkedList(init_list=args[0])
        list2 = LinkedList(init_list=args[1])
        nested = NestedLinkedList(head=Node(list1))
        nested.append(Node(list2))

        result = nested.flatten()
        if result is not None and answer is not None:
            print("input:    " + str(args) + " |\nexpected: " + str(answer) + " |\nresult:   " + str(
                result.to_list()))
            if result.to_list() == answer:
                print("Test case passed!")
            else:
                print("**********************Test with input data:", args, "failed")
        else:
            print("result: " + str(result) + " |\nexpected: " + str(answer))
            if result == answer:
                print("Test case passed!")
            else:
                print("**********************Test with input data:", args, "failed")
        print(result)


# test_flatten()

linked_list = LinkedList(head=Node(1))
linked_list.append(Node(3))
linked_list.append(Node(5))

nested_linked_list = NestedLinkedList(Node(linked_list))

second_linked_list = LinkedList(head=Node(2))
second_linked_list.append(Node(4))

nested_linked_list.append(Node(second_linked_list))

solution = nested_linked_list.flatten()
assert solution.to_list() == [1, 2, 3, 4, 5]
