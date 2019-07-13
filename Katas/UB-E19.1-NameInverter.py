import re


def split_name(name):
    return re.split(r"\s+", name.strip())


def is_honorific(word):
    return re.search(r"^(Mr\.|Mrs\.)", word)


def remove_honorifics(names):
    if len(names) > 1 and is_honorific(names[0]):
        names.pop(0)
    return names


def get_post_nominals(names):
    post_nominals = ""
    if len(names) > 2:
        for x in names[2:]:
            post_nominals += x + " "
    return post_nominals


def format_multi_element_name(names):
    post_nominals = get_post_nominals(names)
    last_name = names[1]
    first_name = names[0]
    reversed_named = "" + last_name + ", " + first_name + " " + post_nominals
    return reversed_named.strip()


def format_name(names):
    if len(names) == 1:
        return names[0]
    else:
        return format_multi_element_name(names)


def name_inverter(name):
    if name is None:
        return ""
    else:
        return format_name(remove_honorifics(split_name(name)))


def test_name_inverter():
    print("--------------------------")
    print("-------test_prime_factors-------")
    test_cases = [
        # degenerate cases first
        (None, ""),                                                 # givenNull_returnEmptyString
        ("", ""),                                                   # givenEmptyString_returnEmptyString
        ("Name", "Name"),                                           # givenOnlyName_returnOnlyName
        # specific cases
        # - spaces
        ("  Name    ", "Name"),                                     # givenOnlyNameWithSpaces_returnOnlyNameWithoutSpaces
        ("   First    Last   ", "Last, First"),                     # givenFirstLastWithSpaces_returnLastFirst
        # -
        ("First Last", "Last, First"),                              # givenFirstLast_returnLastFirst
        ("Mr. First Last", "Last, First"),                          # ignoreHonorifics
        ("Mrs. First Last", "Last, First"),                         # ignoreHonorific
        ("First Last Sr.", "Last, First Sr."),                      # postNominal_stayAtEnd
        ("First Last Sr. BS. Phd.", "Last, First Sr. BS. Phd."),    # postNominals_stayAtEnd
        ("     First      Last     Sr.    BS.    Phd.   ", "Last, First Sr. BS. Phd."),    # integration

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
