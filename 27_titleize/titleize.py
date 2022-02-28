def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    capz_phrase = list(phrase.capitalize())
    i = 1
    while i < len(capz_phrase):
        if capz_phrase[i - 1] == ' ':
            capz_phrase[i] = capz_phrase[i].upper()
        i += 1
    return ''.join(capz_phrase)