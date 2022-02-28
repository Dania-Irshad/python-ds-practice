def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    lst = [char for char in phrase]
    lst[0] = lst[0].upper()
    return ''.join(lst)