'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # n = len(arr)

    # for i in range(n): 
    #     j = 0
    #     while(j < n): 
    #         if (i != j and arr[i] == arr[j]): 
    #             break
    #         j += 1
    #     if (j == n): 
    #         return arr[i] 
      
    # return -1

    s= set()

    for x in arr:
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    return list(s)[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")