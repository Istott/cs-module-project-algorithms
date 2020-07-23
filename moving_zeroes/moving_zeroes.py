'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # for i in arr:
    #     if i > 0 or i < 0:
    #         arr[i], arr[-1] = arr[-1], arr[i]
    
    # res = arr[::-1]
    # return res

    count = 0 # Count of non-zero elements 
    n = len(arr)
      
    for i in range(n): 
        if arr[i] != 0: 
            arr[count] = arr[i] 
            count+=1

    while count < n: 
        arr[count] = 0
        count += 1

    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")