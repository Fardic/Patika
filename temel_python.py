def flatten(nested_list, out=None):
    """
    Recursive function flattens the given nested list
    :param nested_list: Input Nested List
    :param out: Empty List for Recursion Output (Default Parameter is Necessary)
    :return: Flatten List (Same as out)
    """
    if out is None:
        out = []
    for e in nested_list:
        if type(e) == list:
            flatten(e, out)
        else:
            out.append(e)
    return out


def reversal(input_list):
    """
    Void recursive function that reverses and changes its own input list
    :param input_list: Input List
    """
    input_list.reverse()
    for e in input_list:
        if type(e) == list:
            reversal(e)


if __name__ == "__main__":
    # First Question Test Code
    ex = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
    flattened_list = flatten(ex)
    print(flattened_list)

    # Second Question Test Code
    ex2 = [[1, 2], [3, 4], [5, 6, 7]]
    reversal(ex2)
    print(ex2)
