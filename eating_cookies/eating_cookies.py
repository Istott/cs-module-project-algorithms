'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache = None):
    # Your code here
    # a, b, c = 1, 0 , 0

    # for _ in range(n):
    #     a, b, c = a+b+c, a, b
    
    # return a

    if n < 0:
        return 0
    if n == 0:
        return 1
    elif n in cache:
        return cache[n]
    else:
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
        return cache[n]




if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 50
    cache = {i: 0 for i in range(num_cookies+1)}

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
