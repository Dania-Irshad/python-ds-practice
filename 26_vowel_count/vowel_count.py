def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    frequency_dict = {}
    lower_phrase = phrase.lower()
    for char in lower_phrase:
        if char not in frequency_dict and char in vowels:
            frequency_dict[char] = lower_phrase.count(char)
    return frequency_dict