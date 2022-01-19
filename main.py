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
    
