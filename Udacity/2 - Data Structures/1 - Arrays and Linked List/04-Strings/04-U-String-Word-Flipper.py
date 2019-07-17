def word_flipper(our_string):
    split_string = our_string.split(" ")
    flipped_word = ""
    for word in split_string:
        for i in range(len(word) - 1, -1, -1):
            flipped_word += word[i]
        flipped_word += " "
    return flipped_word.strip()


print("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")


def word_flipper(our_string):

    """
    Flip the individual words in a sentence

    Args:
       our_string(string): Strings to have individual words flip
    Returns:
       string: String with words flipped
    """

    word_list = our_string.split(" ")

    for idx in range(len(word_list)):
        word_list[idx] = word_list[idx][::-1]

    return " ".join(word_list)