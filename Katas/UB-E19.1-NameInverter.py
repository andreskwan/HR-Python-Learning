import re


def split_name(name):
    return re.split(r"\s+", name.strip())


def is_honorific(word):
    return re.search(r"^(Mr\.|Mrs\.)", word)


def get_postNominals(param):
    postnominals = ""
    for x in param[2:]:
        postnominals += x + " "
    return postnominals


def name_inverter(name):
    if name is None:
        return ""
    # TPP 6 variable to array
    names = split_name(name)
    if len(names) > 1 and is_honorific(names[0]):
        names.pop(0)
    if len(names) == 1:
        return names[0]
    else:
        postnominals = ""
        if len(names) > 2:
            postnominals = get_postNominals(names)
        reversed_name = "" + names[1] + ", " + names[0] + " " + postnominals
        return reversed_name.strip()


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
        ("First Last", "Last, First"),  # givenFirstLast_returnLastFirst
        ("Mr. First Last", "Last, First"),  # ignoreHonorifics
        ("Mrs. First Last", "Last, First"),  # ignoreHonorific
        ("First Last Sr.", "Last, First Sr."),  # postNominal_stayAtEnd
        ("First Last Sr. BS. Phd.", "Last, First Sr. BS. Phd."),  # postNominal_stayAtEnd

    ]

    args: str
    for (args, answer) in test_cases:
        print("\n---------------------")
        result = name_inverter(args)

        if result is not None and answer is not None:
            print("input:    " + str(args) + " |\nexpected: " + str(answer) + " |\nresult:   " + str(
                result) + " |")
            if result == answer:
                print("Test case passed!")
            else:
                print("Test with input data:", args, "failed")
        else:
            print("result: " + str(result) + " |\nexpected: " + str(answer))
            if result == answer:
                print("Test case passed!")
            else:
                print("Test with input data:", args, "failed")


test_name_inverter()
