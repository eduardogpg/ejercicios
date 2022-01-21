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


def pilas(num):
    '''
    We are making n stone piles! The first pile has n stones. If n is even,
    then all piles have an even number of stones. If n is odd, all piles have
    an odd number of stones. Each pile must more stones than the previous pile
    but as few as possible. Write a Python program to find the number of stones
    in each pile.
    
    >>> pilas(2)
    [2, 4]
    
    >>> pilas(10)
    [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
    
    >>> pilas(3)
    [3, 5, 7]
    
    >>> pilas(17)
    [17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
    
    '''
    return [num + x * 2 for x in range(num)]
