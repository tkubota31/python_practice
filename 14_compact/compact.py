def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    lst_copy =[]
    for val in lst:
        if val:
            lst_copy.append(val)
    return lst_copy

    # return [val for val in lst if val]
