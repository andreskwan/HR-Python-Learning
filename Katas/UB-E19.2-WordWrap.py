def word_wrap(string, width):
    if string is None:
        return ""
    if width is None:
        return string
    if len(string) <= width:
        return string
    else:
        # insert \n according to width
        n = 0
        s = ""
        while (width * (n + 1)) < len(string):
            part_of_string = string[width * n:width * (n + 1)]
            if part_of_string == " ":
                n += 1
                part_of_string = string[width * n:width * (n + 1)]
            else:
                s += part_of_string + "\n"
                n += 1
        s += part_of_string
        return s


def test_word_wrap():
    print("--------------------------")
    print("-------test_prime_factors-------")
    test_cases = [
        # degenerate cases first
        # ((None, None), ""),
        # (("", None), ""),
        # (("x", None), "x"),
        # (("x", 1), "x"),
        # (("xx", 1), "x\nx"),                # breaking a word longer than width
        # (("xxx", 1), "x\nx\nx"),            # multiple lines - breaking a word longer than width
        (("x x", 1), "x\nx"),               # avoiding spaces
        # specific cases
        # (("xxxxx", 1), "x\nx\nx\nx\nx"),    # multiple lines - breaking a word longer than width
        # (("xxxxx", 2), "xx\nxx\nx"),  # multiple lines - breaking a word longer than width
        # integration test

    ]

    args: str
    for (args, answer) in test_cases:
        print("\n---------------------")
        width = args[1]
        string = args[0]
        result = word_wrap(string, width)

        if result is not None and answer is not None:
            print("input:    " + str(args) + " |\nexpected: " + str(answer) + " |\nresult:   " + str(
                result) + " |")
            if result == answer:
                print("Test case passed!")
            else:
                print("**********************Test with input data:", args, "failed")
        else:
            print("result: " + str(result) + " |\nexpected: " + str(answer) + "|")
            if result == answer:
                print("Test case passed!")
            else:
                print("**********************Test with input data:", args, "failed")


test_word_wrap()
