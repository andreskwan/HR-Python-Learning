import re


def name_inverter(name):
    if name is None:
        return ""
    # TPP 11 assign
    name = name.strip()
    # TPP 6 variable to array
    names = re.split(r"\s+", name)
    if len(names) == 1:
        return name
    return "" + names[1] + ", " + names[0]


def test_name_inverter():
    print("--------------------------")
    print("-------test_prime_factors-------")
    test_cases = [
        # degenerate cases first
        (None, ""),  # givenNull_returnEmptyString
        ("", ""),  # givenEmptyString_returnEmptyString
        ("Name", "Name"),  # givenOnlyName_returnOnlyName
        ("  Name    ", "Name"),  # givenOnlyNameWithSpaces_returnOnlyNameWithoutSpaces
        # specific cases
        ("   First    Last   ", "Last, First"),  # givenFirstLastWithSpaces_returnLastFirst
        ("First Last", "Last, First"),  # givenFirstLast_returnLastFirst

    ]

    args: str
    for (args, answer) in test_cases:
        print("\n---------------------")
        result = name_inverter(args)

        if result is not None and answer is not None:
            print("input: " + str(args) + "\nexpected: " + str(answer) + "\nresult: " + str(
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
