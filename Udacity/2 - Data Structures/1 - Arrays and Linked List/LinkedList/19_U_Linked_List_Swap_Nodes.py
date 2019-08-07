class Node:
    """LinkedListNode class to be used for this problem"""

    def __init__(self, data):
        self.data = data
        self.next = None


# helper functions for testing purpose
def create_linked_list(arr):
    if arr is None:
        return None
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head


def to_list(head):
    if head is None:
        return None
    out = []
    node = head
    while node:
        out.append(node.data)
        node = node.next
    return out


def size(head):
    current = head
    count = 0
    while current:
        count += 1
        current = current.next
    return count


def swap_nodes(head, left_index, right_index):
    """
    :param: head- head of input linked list
    :param: left_index - indicates position
    :param: right_index - indicates position
    return: head of updated linked list with nodes swapped
    TODO: complete this function and swap nodes present at left_index and right_index
    Do not create a new linked list
    """
    # I'm giving and order
    # why?
    # to understand where should go each node when assembled
    left_list = None
    right_list = None

    if head is None:
        return []

    if left_index is None:
        return head

    if right_index is None:
        return head

    if left_index == right_index:
        return head

    if left_index >= right_index:
        temp = left_index
        left_index = right_index
        right_index = temp

    # no asumir - no poner mi mente en el algoritmo
    # usar todos los parametros

    original_size = size(head)
    if original_size >= 2:
        left_list = get_left_list(head, left_index, right_index)

        if left_index == 0:
            head = left_list
            return head

        previous_right = get_previous_node(head, left_index)
        previous_right.next = left_list
        return head
    return head


def get_left_list(head, left_index, right_index):
    right_list, counter = get_list_right_node(head, left_index)
    new_index = right_index - counter
    left_list = get_list_left_node(right_list, new_index)
    return left_list


def get_previous_node(list, index):
    if size(list) == 1:
        return None
    if index == 0:
        return None
    counter = 0
    previous_right = list
    while counter < index - 1:
        counter += 1
        previous_right = previous_right.next
    return previous_right


def get_list_right_node(head, left_index):
    counter = 0
    right_node = head
    while counter < left_index:  # find right node
        counter += 1
        right_node = right_node.next
    return right_node, counter + 1


def get_list_left_node(right_node, right_index):
    left_node = None
    # 2) find right_node
    right_node_tail = right_node.next
    right_node.next = None

    # 2) find left_node
    previous_node = get_previous_node(right_node_tail, right_index)

    if previous_node is None:
        left_node = right_node_tail
    else:
        left_node = previous_node.next
        previous_node.next = None

    # 3) preserve left_node_tail
    left_node_tail = left_node.next
    left_node.next = None  # 3->N

    # 4) assemble list
    if previous_node is None:
        right_node.next = left_node_tail
        left_node.next = right_node
    else:
        previous_node.next = right_node
        if left_node_tail is not None:
            right_node.next = left_node_tail
        left_node.next = previous_node
    return left_node


# Solution

def swap_nodes_udacity(head, left_index, right_index):
    if head is None:
        return []

    if left_index is None:
        return head

    if right_index is None:
        return head

    if left_index == right_index:
        return head

    # if both the indices are same
    if left_index == right_index:
        return head

    left_previous = None
    left_current = None

    right_previous = None
    right_current = None

    count = 0
    temp = head
    new_head = None

    # find out previous and current node at both the indices
    while temp is not None:
        if count == left_index:
            left_current = temp
        elif count == right_index:
            right_current = temp
            break

        if left_current is None:
            left_previous = temp
        right_previous = temp
        temp = temp.next
        count += 1

    right_previous.next = left_current
    temp = left_current.next
    left_current.next = right_current.next

    # if both the indices are next to each other
    if left_index != right_index:
        right_current.next = temp

    # if the node at first index is head of the original linked list
    if left_previous is None:
        new_head = right_current
    else:
        left_previous.next = right_current
        new_head = head

    return new_head


def test_swap_nodes():
    print("\n--------------------------")
    print("-------test_swap_nodes-------")

    test_cases = [
        # degenerate cases first
        ((None, None, None), []),
        (([1], None, None), [1]),
        (([1], 1, None), [1]),
        (([], None, 1), []),
        (([], 0, 1), []),  # if empty list return original list
        (([1, 2], 0, 0), [1, 2]),  # if i == j return original list
        (([1, 2], 1, 1), [1, 2]),  # if i == j return original list

        # specific cases
        (([1, 2], 0, 1), [2, 1]),
        (([1, 2], 1, 0), [2, 1]),  # if right_index is 0 return original list

        (([1, 2, 3], 0, 1), [2, 1, 3]),
        (([1, 2, 3], 1, 0), [2, 1, 3]),
        (([1, 2, 3], 1, 2), [1, 3, 2]),
        (([1, 2, 3], 2, 1), [1, 3, 2]),

        # get_previous_right
        (([1, 2, 3, 4], 0, 1), [2, 1, 3, 4]),
        (([1, 2, 3, 4], 1, 0), [2, 1, 3, 4]),
        (([1, 2, 3, 4], 1, 2), [1, 3, 2, 4]),
        (([1, 2, 3, 4], 2, 1), [1, 3, 2, 4]),
        (([1, 2, 3, 4], 2, 3), [1, 2, 4, 3]),
        (([1, 2, 3, 4], 3, 2), [1, 2, 4, 3]),

        # right_index
        (([1, 2, 3], 0, 2), [3, 2, 1]),
        (([1, 2, 3], 2, 0), [3, 2, 1]),
        (([1, 2, 3, 4], 0, 1), [2, 1, 3, 4]),
        (([1, 2, 3, 4], 1, 2), [1, 3, 2, 4]),
        (([1, 2, 3, 4], 2, 3), [1, 2, 4, 3]),
        (([1, 2, 3, 4], 0, 2), [3, 2, 1, 4]),
        (([1, 2, 3, 4], 2, 0), [3, 2, 1, 4]),
        #
        # # Udacity cases
        (([3, 4, 5, 2, 6, 1, 9], 0, 1), [4, 3, 5, 2, 6, 1, 9]),
        (([3, 4, 5, 2, 6, 1, 9], 3, 4), [3, 4, 5, 6, 2, 1, 9]),
        (([3, 4, 5, 2, 6, 1, 9], 2, 4), [3, 4, 6, 2, 5, 1, 9]),
        # integration test

    ]
    for (args, answer) in test_cases:
        print("\n---------------------")
        # linkedList = LinkedList(init_list=args)
        list_head = create_linked_list(args[0])
        left_index = args[1]
        right_index = args[2]
        # result_list = to_list(swap_nodes(list_head, left_index, right_index))
        result_list = to_list(swap_nodes(list_head, left_index, right_index))

        if result_list is not None and answer is not None:
            print("input:    " + str(args) + " |\nexpected: " + str(answer) + " |\nresult:   "
                  + str(result_list) + " |")
            if result_list == answer:
                print("Test case passed!")
            else:
                print("**********************Test with input data:", args, "failed")
        else:
            print("result: " + str(result_list) + " |\nexpected: " + str(answer) + "|")
            if result_list == answer:
                print("Test case passed!")
            else:
                print("**********************Test with input data:", args, "failed")


test_swap_nodes()
