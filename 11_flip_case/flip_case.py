def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    to_swap=to_swap.upper()
    new_str = ""
    for char in phrase:
        if char.upper() == to_swap:
            char = char.swapcase()
        new_str += char

    return new_str
