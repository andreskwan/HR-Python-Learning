class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        #tail
        #count

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

    def print_linked_list(self):
        # #  1 identify the last node.
        # # the last node is the one that points to None
        # if self.next is None:
        #     self.next = node
        #     return
        actual_node = self.head
        while actual_node:
            print(actual_node.value)
            actual_node = actual_node.next
        return

    def to_list(self):
        output_list = []
        # if self.head is None:
        #     return output_list
        current_node = self.head
        while current_node:
            output_list.append(current_node.value)
            current_node = current_node.next
        return output_list



# Test your method here
linked_list = LinkedList()
linked_list.append(3)
linked_list.append(2)
linked_list.append(-1)
linked_list.append(0.2)
print(linked_list.print_linked_list())
print(linked_list.to_list())

print ("Pass" if(linked_list.to_list() == [3, 2, -1, 0.2]) else "Fail")


def print_linked_list(self):
    # #  1 identify the last node.
    # # the last node is the one that points to None
    # if self.next is None:
    #     self.next = node
    #     return
    actual_node = self
    while actual_node is not None:
        print(actual_node.value)
        actual_node = actual_node.next


def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    if len(input_list) == 0:
        return None

    main_node = Node(input_list[0])
    for index in range(1,len(input_list) - 1):
        # every time we are going to add a new node
        # we are looking for the tail!
        main_node.append(Node(input_list[index]))
    return main_node


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
    return head2


def create_linked_list_udacity(input_list):
    head = None
    tail = None

    for value in input_list:
        if head is None:
            head = Node(value)
            tail = head  # with one value tail and head are the same.
        else:
            tail.next = Node(value)  # add new node
            tail = tail.next  # update tail
    return head


# ### Test Code
# def test_function(input_list, head):
#     # try:
#         if len(input_list) == 0:
#             if head is not None:
#                 print("Fail")
#                 return
#         for value in input_list:
#             if head.value != value:
#                 print("Fail")
#                 return
#             else:
#                 head = head.next
#         print("Pass")
#     # except Exception as e:
#     #     print("Fail: " + e)


input_list = [1, 2, 3, 4, 5, 6]
# head = create_linked_list(input_list)
head = create_linked_list_better(input_list)
print_linked_list(head)
# test_function(input_list, head)

input_list = [1]
# head = create_linked_list(input_list)
head = create_linked_list_better(input_list)
# test_function(input_list, head)
print_linked_list(head)

input_list = []
# head = create_linked_list(input_list)
head = create_linked_list_better(input_list)
# test_function(input_list, head)
print_linked_list(head)

input_list = [441.,  65.,  90., 441., 122.,  88.,  61.,  81., 104., 108.,  90.,
        90.,  72., 169., 173., 101.,  68.,  57.,  54.,  83.,  90., 122.,
        86., 358., 135., 106., 146.,  63.,  68.,  57.,  98., 270.,  59.,
        50., 101.,  68.,  54.,  81.,  63.,  67., 180.,  77.,  54.,  57.,
        52.,  61.,  95.,  79., 133.,  63., 181.,  68., 216., 135.,  71.,
        54., 124., 155., 113.,  95.,  58.,  54.,  86.,  90.,  52.,  92.,
        90.,  59.,  61., 104.,  86.,  88.,  97.,  68.,  56.,  77., 230.,
       495.,  86.,  55.,  97., 110., 135.,  61.,  99.,  52.,  90.,  59.,
       158.,  74.,  81., 108.,  90., 116., 108.,  74.,  74.,  86.,  61.,
        61.,  62.,  97.,  63.,  81.,  50.,  55.,  54.,  86., 170.,  70.,
        78., 225.,  67.,  79.,  99., 104.,  50., 173.,  88.,  68.,  52.,
        90.,  81., 817.,  56., 135.,  27.,  52.,  90.,  95.,  91., 178.,
       101.,  95., 383.,  90., 171., 187., 132.,  89., 110.,  81.,  54.,
        63., 412., 104., 306.,  56.,  74.,  59.,  80.,  65.,  57., 203.,
        95., 106.,  88.,  96., 108.,  50.,  18.,  56.,  99.,  56.,  91.,
        81.,  88.,  86.,  52.,  81.,  45.,  92., 104., 167.,  16.,  81.,
        77.,  86.,  99., 630., 268.,  50.,  62.,  90., 270., 115.,  79.,
        88.,  83.,  77.,  88.,  79.,   4.,  95.,  90.,  79.,  63.,  79.,
        89., 104.,  57.,  61.,  88.,  54.,  65.,  81., 225., 158.,  61.,
        81., 146.,  83.,  48.,  18., 630.,  77.,  59.,  58.,  77., 119.,
       207.,  65.,  65.,  81.,  54.,  79., 191.,  79.,  14.,  77.,  52.,
        55.,  56., 113.,  90.,  88.,  86.,  49.,  52., 855.,  81., 104.,
        72., 356., 324., 203.,  97.,  99., 106.,  18.,  79.,  58.,  63.,
        59.,  95.,  54.,  65.,  95., 360., 230., 288., 236.,  36., 191.,
        77.,  79., 383.,  86., 225.,  90.,  97.,  52., 135.,  56.,  81.,
       110.,  72.,  59.,  54., 140.,  72.,  90.,  90.,  86.,  77., 101.,
        61.,  81.,  86., 128.,  61., 338., 248.,  90., 101.,  59.,  79.,
        79.,  72.,  70., 158.,  61.,  70.,  79.,  54., 125.,  85., 101.,
        54.,  83.,  99.,  88.,  79.,  83.,  86., 293., 191.,  65.,  69.,
       405.,  59., 117.,  89.,  79.,  54.,  52.,  87.,  80.,  55.,  50.,
        52.,  81., 234.,  86.,  81.,  70.,  90.,  74.,  68.,  83.,  79.,
        56.,  97.,  50.,  70., 117.,  83.,  81., 630.,  56., 108., 146.,
       320.,  85.,  72.,  79., 101.,  56.,  38.,  25.,  54., 104.,  63.,
       171.,  61., 203., 900.,  63.,  74., 113.,  59., 310.,  87., 149.,
        54.,  50.,  79.,  88., 315., 153.,  79.,  52., 191., 101.,  50.,
        92.,  72.,  52., 180.,  49., 437.,  65., 113., 405.,  54.,  56.,
        74.,  59.,  55.,  58.,  81.,  83.,  79.,  71.,  62.,  63., 131.,
        91.,  57.,  77.,  68.,  77.,  54., 101.,  47.,  74., 146.,  99.,
        54., 443., 101., 225., 288., 143., 101.,  74., 288., 158., 203.,
        81.,  54.,  76.,  97.,  81.,  59.,  86.,  82., 105., 331.,  58.,
        54.,  56., 214.,  79.,  73., 117.,  50., 334.,  52.,  71.,  54.,
        41., 135., 135.,  63.,  79., 162.,  95.,  54., 108.,  67., 158.,
        50.,  65., 117.,  39., 473., 135.,  51., 171.,  74., 117.,  50.,
        61.,  95.,  83.,  52.,  17.,  57.,  81.]
# head = Node(2)
# head.next = Node(1)
# head = Node(2)
# head.append(Node(1))
# head.append(Node(4))
# head.append(Node(3))
# head.append(Node(5))


# print(head.next.value)
# print(head.next.next.value)
# print(head.next.next.next.value)

# head.print_linked_list()




