'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
import collections

def sliding_window_max(nums, k):
    # Your code here
    n = len(nums)
    # max = 0
    newArr = []

    # for i in range(n - k + 1): 
    #     max = nums[i] 
    #     for j in range(1, k): 
    #         if nums[i + j] > max: 
    #             max = nums[i + j] 
    #             newArr.append(max)

    # return newArr

    #     """ Create a Double Ended Queue, Qi that  
    # will store indexes of array elements.  
    # The queue will store indexes of useful  
    # elements in every window and it will 
    # maintain decreasing order of values from 
    # front to rear in Qi, i.e., arr[Qi.front[]] 
    # to arr[Qi.rear()] are sorted in decreasing 
    # order"""
    Qi = collections.deque() 
      
    # Process first k (or first window)  
    # elements of array 
    for i in range(k): 
        
        # For every element, the previous  
        # smaller elements are useless 
        # so remove them from Qi 
        while Qi and nums[i] >= nums[Qi[-1]] : 
            Qi.pop() 
          
        # Add new element at rear of queue 
        Qi.append(i); 
          
    # Process rest of the elements, i.e.  
    # from arr[k] to arr[n-1] 
    for i in range(k, n): 
          
        # The element at the front of the 
        # queue is the largest element of 
        # previous window, so print it 
        # print(str(nums[Qi[0]]) + " ", end = "") 
        newArr.append(nums[Qi[0]])
          
        # Remove the elements which are  
        # out of this window 
        while Qi and Qi[0] <= i-k: 
              
            # remove from front of deque 
            Qi.popleft()  
          
        # Remove all elements smaller than 
        # the currently being added element  
        # (Remove useless elements) 
        while Qi and nums[i] >= nums[Qi[-1]] : 
            Qi.pop() 
          
        # Add current element at the rear of Qi 
        Qi.append(i) 
      
    # Print the maximum element of last window 
    # print(str(arr[Qi[0]])) 
    newArr.append(nums[Qi[0]])
        
    return newArr

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
