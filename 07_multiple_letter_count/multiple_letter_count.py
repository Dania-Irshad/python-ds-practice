def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    ltr_dict = {}
    for char in phrase:
        if char not in ltr_dict.keys():
            ltr_dict.update({char: phrase.count(char)})
    return ltr_dict