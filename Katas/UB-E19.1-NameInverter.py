import re


def is_honorific(word):
    return word == "Mr."


def name_inverter(name):
    if name is None:
        return ""
    # TPP 6 variable to array
    names = split_name(name)
    if len(names) > 1 and is_honorific(names[0]):
        names.pop(0)
    if len(names) == 1:
        return names[0]
    return "" + names[1] + ", " + names[0]


def split_name(name):
    return re.split(r"\s+", name.strip())


def test_name_inverter():
    print("--------------------------")
    print("-------test_prime_factors-------")
    test_cases = [
        # degenerate cases first
        (None, ""),  # givenNull_returnEmptyString
        ("", ""),  # givenEmptyString_returnEmptyString
        ("Name", "Name"),  # givenOnlyName_returnOnlyName
        # specific cases
        # - spaces
        ("  Name    ", "Name"),  # givenOnlyNameWithSpaces_returnOnlyNameWithoutSpaces
        ("   First    Last   ", "Last, First"),  # givenFirstLastWithSpaces_returnLastFirst
        # -
        ("First Last", "Last, First"),      # givenFirstLast_returnLastFirst
        ("Mr. First Last", "Last, First"),  # ignoreHonorific

    ]

    args: str
    for (args, answer) in test_cases:
        print("\n---------------------")
        result = name_inverter(args)

        if result is not None and answer is not None:
            print("input:    " + str(args) + "\nexpected: " + str(answer) + "\nresult:   " + str(
                result))
            if result == answer:
                print("Test case passed!")
            else:
                print("Test with input data:", args, "failed")
        else:
            print("result: " + str(result) + "\nexpected: " + str(answer))
            if result == answer:
                print("Test case passed!")
            else:
                print("Test with input data:", args, "failed")


test_name_inverter()
