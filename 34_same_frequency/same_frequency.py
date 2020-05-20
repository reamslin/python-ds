def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    str1 = str(num1)
    str2 = str(num2)

    set1 = set(str1)
    set2 = set(str2)

    if set1.difference(set2):
        return False
    else:
        for n in set1:
            if str1.count(n) != str2.count(n):
                return False
        return True
