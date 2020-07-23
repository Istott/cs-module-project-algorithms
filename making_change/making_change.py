#!/usr/bin/python

import sys

def making_change(amount, denominations):
  # Your code here

    size = len(denominations)

    # Declaring a 2-D array
    # for storing solutions to subproblems:
    arr = [[0] * (amount + 1) for x in range(size + 1)]

    # Initializing first column of array to 1
    # because a sum of 0 can be made
    # in one possible way: {0}
    for i in range(size + 1):
        arr[i][0] = 1

    # Applying the recursive solution:
    for i in range(1, size + 1):
        for j in range(1, amount + 1):
            if denominations[i - 1] > j:  # Cannot pick the highest coin:
                arr[i][j] = arr[i - 1][j]
            else:  # Pick the highest coin:
                arr[i][j] = arr[i - 1][j] + arr[i][j - denominations[i - 1]]
                
    print(arr)
    return arr[size][amount] 

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")