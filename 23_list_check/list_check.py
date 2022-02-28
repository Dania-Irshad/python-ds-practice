def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    type_list = True
    for item in lst:
        if type(item) != list:
            type_list = False
            break
        else:
            type_list = True
    return type_list
