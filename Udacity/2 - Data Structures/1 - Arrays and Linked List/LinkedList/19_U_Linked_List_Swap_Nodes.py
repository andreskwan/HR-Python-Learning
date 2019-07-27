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
    return None


def test_swap_nodes():
    print("\n--------------------------")
    print("-------test_swap_nodes-------")

    test_cases = [
        # degenerate cases first
        ((None, None, None), []),
        # (([1], None, None), [1]),
        # (([1], 1, None), [1]),
        # (([], None, 1), []),
        # (([], 0, 1), []),  # if empty list return original list
        # (([], 1, 1), []),  # if empty list return original list
        # (([1, 2], 1, 0), [1, 2]),  # if right_index is 0 return original list

        # specific cases

        # Udacity cases

        # integration test

    ]
    for (args, answer) in test_cases:
        print("\n---------------------")
        # linkedList = LinkedList(init_list=args)
        list_head = create_linked_list(args[0])
        left_index = args[1]
        right_index = args[2]
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
