def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    lst = []

    for char in phrase:
        if to_swap.isupper():
            if to_swap == char:
                lst.append(char.lower())
            elif to_swap.lower() == char:
                lst.append(char.upper())
            else:
                lst.append(char)
        elif to_swap.islower():
            if to_swap == char:
                lst.append(char.upper())
            elif to_swap.upper() == char:
                lst.append(char.lower())
            else:
                lst.append(char)
    
    return ''.join(lst)