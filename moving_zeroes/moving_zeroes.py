'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here

    # newArr = [arr[i - 1] for i in arr if i > 0]

    for i in arr:
        if i > 0 or i < 0:
            arr[i], arr[-1] = arr[-1], arr[i]
    
    res = arr[::-1]
    
    return res


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")