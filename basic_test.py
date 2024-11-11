def int_division():
    """
    Task:
    - Perform integer division of 7 by 2.
    
    Return:
    - The result of the division (integer).
    """
    return 7//2
    pass


def float_multiplication():
    """
    Task:
    - Multiply 3.0 by 2.
    
    Return:
    - The result of the multiplication (float).
    """
    return 3.0 * 2
    pass


def combine_operations():
    """
    Task:
    - Add the result of integer division and multiplication.
    
    Return:nested['b'] = [nested['b'][0],nested['b'][1]]
    nested['b'].append(6)
    return nested
    - The combined result (float).
    """
    result = int_division() + float_multiplication()
    return result
    pass


def extract_word():
    """
    Task:
    - Extract the word 'awesome' from the string 'Python is awesome!'.
    
    Return:
    - The extracted word ('awesome').
    """
    string1 = 'Python is awesome!'
    if 'awesome' in string1:
        return 'awesome'
    pass


def to_lowercase():
    """
    Task:
    - Convert the string 'Python is awesome!' to lowercase.
    
    Return:
    - The lowercase version of the string.
    """
    string1 = 'Python is awesome!'
    return string1.lower()
    pass


def count_o():
    """
    Task:
    - Count how many times the letter 'o' appears in the string 'Python is awesome!'.
    
    Return:
    - The count of the letter 'o'.
    """
    string1 = 'Python is awesome!'
    return string1.count('o')
    pass


def evaluate_boolean():
    """
    Task:
    - Evaluate the expression 'not (5 > 3) and (10 == 5 * 2)'.
    
    Return:
    - The boolean result of the expression.
    """
    exp1 = not (5 > 3)
    exp2 = 10 == 5 * 2
    return exp1 and exp2
    pass
