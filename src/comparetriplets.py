# problem statement
# Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.
# The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).
# The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].
# If a[i] > b[i], then Alice is awarded 1 point.
# If a[i] < b[i], then Bob is awarded 1 point.
# If a[i] = b[i], then neither person receives a point. Comparison points are the total points a person earned.
# Given a and b, determine their respective comparison points.

# solution
# After reading the problem, we can observe 2 things:

# The comparison array must come with Alice score first.
# If both ratings are equal, nobody receives a point.



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

