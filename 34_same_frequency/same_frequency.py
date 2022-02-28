def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    i = 0
    num1_str = str(num1)
    num2_str = str(num2)
    while i < len(num1_str):
        if num1_str.count(num1_str[i]) != num2_str.count(num1_str[i]):
            return False
        i += 1
    return True