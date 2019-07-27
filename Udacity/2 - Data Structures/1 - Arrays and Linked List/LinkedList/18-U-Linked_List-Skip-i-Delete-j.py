# LinkedList Node class for your reference
class Node:
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


def skip_i_delete_j(list_head, i, j):
    """
        :param: head - head of linked list
        :param: i - first `i` nodes that are to be skipped
        :param: j - next `j` nodes that are to be deleted
        return - return the updated head of the linked list
        """
    next = None
    if list_head is None:
        return []
    if i is None:
        return list_head
    if i is 0:
        return list_head
    if i > size(list_head):
        return list_head
    if j is None:
        return list_head
    if j is 0:
        return list_head

    available = size(list_head) - i
    i_counter = 1
    i_current = list_head

    while i_counter < i:     # find i-1 node // start to delete from node i
        i_current = i_current.next
        i_counter += 1

    j_head = i_current.next  # preserve nodes after i_current
    i_current.next = None    # keep nodes from list_heat up to i_current

    j_counter = 0
    j_current = j_head       # it is copied or referenced? Reference
    new_j = j if j <= available else available

    while j_counter < new_j:
        j_counter += 1
        if j_current.next is not None:
            j_current = j_current.next
        else:
            j_current = None

    i_current.next = skip_i_delete_j(j_current, i, j)
    return list_head


def test_skip_i_delete_j():
    print("--------------------------")
    print("-------test_skip_i_delete_j-------")

    test_cases = [
        # degenerate cases first
        ((None, None, None), []),
        (([1], None, None), [1]),
        (([1], 1, None), [1]),
        (([], None, 1), []),
        (([], 0, 1), []),                             # if empty list return original list
        (([], 1, 1), []),                             # if empty list return original list
        (([1, 2], 1, 0), [1, 2]),                     # if j is 0 return original list

        # specific cases
        (([1, 2], 0, 1), [1, 2]),                        # i can not be 0 - return original list
        (([1, 2], 1, 1), [1]),                        # if i and j are equal - is valid
        (([1, 2], 1, 2), [1]),                        # j can be greater than (length - i) return what is left
        (([1, 2], 1, 3), [1]),                        # j can be greater than (length - i) return what is left
        (([1, 2], 2, 3), [1, 2]),                     # if i is equal to the length of the list - return original list
        (([1, 2], 3, 1), [1, 2]),                     # if i greater than length of the list - return original list
        (([1, 2, 3], 1, 1), [1, 3]),                  # if i and j are equal - is valid
        (([1, 2, 3], 2, 1), [1, 2]),                  # i greater than j - is valid
        # evaluate | j << (len(list) - i)
        (([1, 2, 3, 4], 1, 1), [1, 3]),               # i greater than j - is valid
        (([1, 2, 3, 4], 3, 1), [1, 2, 3]),            # i greater than j - is valid
        (([1, 2, 3, 4, 5], 1, 1), [1, 3, 5]),
        (([1, 2, 3, 4, 5], 1, 2), [1, 4]),
        (([1, 2, 3, 4, 5], 1, 3), [1, 5]),
        (([1, 2, 3, 4, 5], 1, 4), [1]),
        (([1, 2, 3, 4, 5], 2, 1), [1, 2, 4, 5]),
        (([1, 2, 3, 4, 5], 2, 2), [1, 2, 5]),
        (([1, 2, 3, 4, 5], 2, 3), [1, 2]),
        (([1, 2, 3, 4, 5], 2, 4), [1, 2]),
        # Udacity cases
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 2, 2), [1, 2, 5, 6, 9, 10]),
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 2, 3), [1, 2, 6, 7, 11, 12]),

        # integration test

    ]
    for (args, answer) in test_cases:
        print("\n---------------------")
        # linkedList = LinkedList(init_list=args)
        list_head = create_linked_list(args[0])
        i = args[1]
        j = args[2]
        result_list = to_list(skip_i_delete_j(list_head, i, j))

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


test_skip_i_delete_j()
