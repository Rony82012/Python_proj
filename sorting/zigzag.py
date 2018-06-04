'''
Example: 
Input:  arr[] = {4, 3, 7, 8, 6, 2, 1}
Output: arr[] = {3, 7, 4, 8, 2, 6, 1}

Input:  arr[] =  {1, 4, 3, 2}
Output: arr[] =  {1, 4, 2, 3}
'''

def zigZag(arr):
    # Flag true indicates relation "<" is expected,
    # else ">" is expected.  The first expected relation
    # is "<"
    n = len(arr)
    flag = True
    for i in range(n-1):
        # "<" relation expected
        if flag is True:
            # If we have a situation like A > B > C,
            #   we get A > B < C 
            # by swapping B and C
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
            # ">" relation expected
        else:
            # If we have a situation like A < B < C,
            #   we get A < C > B
            # by swapping B and C    
            if arr[i] < arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
        flag = bool(1 - flag)
    print(arr)
  
# Driver program
arr = [4, 3, 7, 8, 6, 2, 1]

zigZag(arr)
