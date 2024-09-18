def diagonalDifference(arr):
    """
    This function takes an array of integers and returns the absolute difference
    between the two diagonals of the array.

    Parameters:
    arr (list): A 2D list of integers

    Returns:
    int: The absolute difference between the two diagonals of the array
    """
    
    left,right=0,0
    for i in range(len(arr)):
        left+=arr[i][i]
        right+=arr[i][len(arr)-i-1]
    print(abs(left-right))
    return abs(left-right)
