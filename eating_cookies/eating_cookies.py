'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    a, b, c = 1, 0 , 0

    for _ in range(n):
        a, b, c = a+b+c, a, b
    
    return a


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
