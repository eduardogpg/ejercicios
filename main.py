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
    
    -Args:
        numbers: int
    
    - Return
        Boolean
    
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


def stones(number):
    from functools import reduce
    n = number
    
    """ We are making n stone piles! The first pile has n stones. 
    If n is even, then all piles have an even number of stones. 
    If n is odd, all piles have an odd number of stones. 
    
    Each pile must more stones than the previous pile but as few as possible. 
    Write a Python program to find the number of stones in each pile.
    
    >>> stones(2)
    [2, 4]
    
    >>> stones(10)
    [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
    
    >>> stones(3)
    [3, 5, 7]
    
    >>> stones(17)
    [17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
    """
     
    return reduce(lambda x: x + 2, [x in range(number, number + number)])
    
    # return [x*2+n for x in range(0, n)] = Julian
    # return [ x for x in range(number, number+number+1,2) ] = Mab Music 113


def substring(lista_string):
    """Write a Python program to check the nth-1 string 
    is a proper substring of nth string in a given list of strings.
    
    >>> substring(['a', 'abb', 'sfs', 'oo', 'de', 'sfde'])
    True
    
    >>> substring(['a', 'abb', 'sfs', 'oo', 'ee', 'sfde'])
    False
    
    >>> substring(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew'])
    False
    
    >>> substring(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew'])
    True
    """
    return lista_string[- 2] in lista_string[-1]


def ten(numbers):
    """Write a Python program to test a list of one hundred integers between 0 and 999,
    which all differ by ten from one another. Return true or false
    
    >>> numbers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990]
    >>> ten(numbers)
    True
    
    >>> numbers = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720, 740, 760, 780, 800, 820, 840, 860, 880, 900, 920, 940, 960, 980]
    >>> ten(numbers)
    False
    """
    if len(numbers) < 100:
        return False

    last_element = numbers[0]
    
    for pos in range(1, len(numbers)):
        if last_element + 10 == numbers[pos] and (last_element >= 0 and last_element <= 999):
            last_element = numbers[pos]
        else:
            return False
    
    return True


def one(numbers):
    """Write a Python program to check a given list of integers where the sum of the first i integers is i}
    
    >>> one([0, 1, 2, 3, 4, 5])
    False
    
    >>> one([1, 1, 1, 1, 1, 1])
    True
    
    >>> one([2, 2, 2, 2, 2])
    False
    """
    return numbers[0] == 1


def splits(sentence):
    """Write a Python program to split a string of words separated by commas and spaces into two lists, 
    words and separators. 

    """
    word = ''
    words = list()
    separators = list()
    
    for c in sentence:
        if c  in (' ', ','):
            words.append(word)
            word = ''

            separators.append(c)
        else:
            word = word + c
    
    words.append(word)
    return [words, separators]


def containing(numbers):
    """Write a Python program to find list integers containing exactly four distinct values,
    such that no integer repeats twice consecutively among the first twenty entries.
    
    >>> containing([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4])
    True
    
    >>> containing([1, 1, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4])
    False
    
    >>> containing([1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3])
    False
    
    >>> containing([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
    False
    """
    
    if len(set(numbers)) != 4:
        return False
    
    last_element = numbers[0]
    
    for pos in range(1, len(numbers)):
        if last_element == numbers[pos]:
            return False
        else:
            last_element = numbers[pos]
            
    return True
    
    