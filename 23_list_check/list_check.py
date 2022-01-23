def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    for vals in lst:
        if isinstance(vals,list):
            return True
        else:
            return False
