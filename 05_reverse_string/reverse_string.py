def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    lst = [char for char in phrase]
    lst.reverse()
    return ''.join(lst)
