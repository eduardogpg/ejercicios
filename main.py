def occurrences(numbers):
    """Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five
    
    >>> occurrences([19, 19, 15, 5, 3, 5, 5, 2])
    True
    
    >>> occurrences([19, 15, 15, 5, 3, 3, 5, 2])
    False
    
    >>> occurrences([19, 19, 5, 5, 5, 5, 5])
    True
    """
    return numbers.count(19) == 2 and numbers.count(5) >= 3
    
    
def integers(numbers):
    """Write a Python program that accept a list of integers and check the length and the fifth element. Return true if the length of the list is 8 and fifth element occurs thrice in the said list.
    
    >>> integers([19, 19, 15, 5, 5, 5, 1, 2])
    True
    
    >>> integers([19, 15, 5, 7, 5, 5, 2])
    False
    
    >>> integers([11, 12, 14, 13, 14, 13, 15, 14])
    True
    
    >>> integers([19, 15, 11, 7, 5, 6, 2])
    False
    """
    return len(numbers) == 8 and numbers.count(numbers[4]) >= 3


def mod(number):
    """Write a Python program that accept an integer test whether an integer greater than 4^4 and which is 4 mod 34
    
    >>> mod(922)
    True
    
    >>> mod(914)
    False
    
    >>> mod(854)
    True
    """
    return number > (4**4) and number % 34 == 4