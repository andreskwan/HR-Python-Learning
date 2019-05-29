def string_reverser(our_string):
    length = len(our_string) - 1
    new_str = ""
    for i in range(length, -1, -1):
        new_str += our_string[i]
    return new_str


print('Pass' if ('retaw' == string_reverser('water')) else "Fail")


def string_reverser(our_string):
    """
    Reverse the input string
    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """
    new_string = ""

    # Iterate over old string
    for i in range(len(our_string)):
        # Grab the character from the back of the string and add them to the new string
        new_string += our_string[(len(our_string)-1)-i]
    return new_string


def reverse_array(a):
    length = len(a) - 1
    inverted = []
    for i in range(length, -1, -1):
        inverted.append(a[i])
    return inverted

# swift
 # func reverseArray(a: [Int]) -> [Int] {
 #     // def reverseArray(a):
 #     let lastIndex = a.count - 1
 #     var inverted = [Int]()
 #     for i in stride(from:lastIndex,through:0,by:-1){
 #         inverted.append(a[i])
 #     }
 #     return inverted
 # }