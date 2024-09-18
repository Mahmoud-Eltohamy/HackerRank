def compareTriplets(a, b):
    '''
    Compares two lists of ratings and returns a list of two comparison points.
    
    Parameters:
    a (list): Alice's ratings
    b (list): Bob's ratings
    
    Returns:
    list: A list of two integers in the order [Alice's points, Bob's points]
    '''
    
    alice, bob = 0, 0
    for i in range(0, len(a)):
        if a[i] > b[i]:
            alice+=1
        elif a[i] < b[i]:
            bob+=1
    return [alice, bob]

