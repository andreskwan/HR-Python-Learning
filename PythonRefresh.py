courses = {
    'spring2020': {'cs101': {'name': 'Building a Search Engine', 'teacher': 'Dave', 'assistant': 'Peter C.'},
                   'cs373': {'name': 'Programming a Robotic Car', 'teacher': 'Sebastian', 'assistant': 'Andy'}},
    'fall2020': {'cs101': {'name': 'Building a Search Engine', 'teacher': 'Dave', 'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs', 'teacher': 'Peter N.', 'assistant': 'Andy', 'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog', 'teacher': 'Steve', 'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser', 'teacher': 'Wes', 'assistant': 'Peter C.', 'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car', 'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography', 'teacher': 'Dave'}},
    'spring2044': {'cs001': {'name': 'Building a Quantum Holodeck', 'teacher': 'Dorina'},
                   'cs003': {'name': 'Programming a Robotic Robotics Teacher', 'teacher': 'Jasper'},
                   }
}


# def string_reverser(our_string):
#     print(our_string)
#     length = len(our_string) - 1
#     print(length)
#     inverted = []
#     print([*range(length, -1, -1)])
#     inverted = [x for i in range(length, -1, -1) our_string[i]]
#     # for i in range(length, -1, -1):
#     #     print(our_string[i])
#     #     inverted.append(our_string[i])
#     # print(str(inverted))
#     str1 = ''.join(inverted)
#     return str1

def string_reverser(our_string):
    length = len(our_string) - 1
    inverted = []
    new_str = ""
    for i in range(length, -1, -1):
        # inverted.append(our_string[i])
        new_str += our_string[i]
    str1 = ''.join(inverted)
    # return str1
    return new_str


print ("Pass" if ('retaw' == string_reverser('water')) else "Fail")


def reverseArray(a):
    length = len(a) - 1
    inverted = []
    # new_str = ""
    for i in range(length, -1, -1):
        inverted.append(a[i])
        # new_str += our_string[i]
    # str1 = ''.join(inverted)
    # return str1
    return inverted

# swift
 # func reverseArray(a: [Int]) -> [Int] {
 #  2.     // def reverseArray(a):
 #  3.     let lastIndex = a.count - 1
 #  4.     var inverted = [Int]()
 #  5.     for i in stride(from:lastIndex,through:0,by:-1){
 #  6.         inverted.append(a[i])
 #  7.     }
 #  8.     return inverted
 #  9. }