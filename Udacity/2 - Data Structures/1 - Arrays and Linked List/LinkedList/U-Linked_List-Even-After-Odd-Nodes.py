class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head


def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


def to_list(head):
    out = []
    node = head
    while node:
        out.append(node.data)
        node = node.next
    return out


# Solution
def even_after_odd(current_node):
    if current_node is None:
        return create_linked_list([])

    even = None
    odd = None
    even_tail = None
    head_tail = None

    while current_node:
        next_node = current_node.next

        if current_node.data % 2 == 0:
            if even is None:
                even = current_node
                even_tail = even
            else:
                even_tail.next = current_node
                even_tail = even_tail.next
        else:
            if odd is None:
                odd = current_node
                odd_tail = odd
            else:
                odd_tail.next = current_node
                odd_tail = odd_tail.next
        current_node.next = None
        current_node = next_node

    if odd is None:
        return even
    odd_tail.next = even
    return odd


# return list/head not an array
# def even_after_odd(head):
#     return None


def test_even_after_odd():
    print("--------------------------")
    print("-------test_even_after_od-------")
    test_cases = [
        # degenerate cases first
        # (None, []),
        # ([], []),
        ([1], [1]),
        ([1, 3], [1, 3]),           # only odds
        ([2, 4], [2, 4]),           # only even
        ([1, 2], [1, 2]),           # even after odd
        ([2, 1], [1, 2]),           # even before odd
        ([4, 1, 3], [1, 3, 4]),     # even at the beginning
        ([4, 2, 3], [3, 4, 2]),     # odd at the end
        ([4, 1, 2], [1, 4, 2]),     # odd between even
        ([1, 2, 3], [1, 3, 2]),     # even between odd
        ([1, 3, 5, 7], [1, 3, 5, 7]),
        ([2, 4, 6, 8], [2, 4, 6, 8]),
        ([1, 2, 3, 4, 5, 6], [1, 3, 5, 2, 4, 6]),

        # specific cases

        # integration test
    ]

    for (args, answer) in test_cases:
        print("\n---------------------")
        # linkedList = LinkedList(init_list=args)
        list_head = create_linked_list(args)
        result_list = to_list(even_after_odd(list_head))

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


test_even_after_odd()
