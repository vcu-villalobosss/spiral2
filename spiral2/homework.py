# spiral hw
import math
def spiralize(size, n=1):  
    # finding last number in spiral, squaring
    x = n
    last_num = x ** 2 
    diagonals = []
    reset = 0  

    # distance between diagonals
    y = 4
    dist = y - 1
    
    # creating list for numbers in spiral
    numList = list(range(1, x+1))

    # filter spiral list to include only odd numbers
    numlist_odd = [i for i in numList if i % 2 != 0]

    """ 
    This would be the final section for my solution, however I got stuck. I'm sure I overcomplicated the solution, but idealy I would create a list
    of all the diagonals based off of the pattern I found and sum for the total. My program starts by filtering all the odd numbers in a range that ends with the last diagonal
    and would then create a new list based off of a for loop. I found that the next spiral always begins at a perfect square and as the size of the spiral grows the space in 
    between the next diagonal increments by the size of the spiral (y) - 1. I wasn't able to create a tangible solution yet, however I hope I was able to explain my thought-process.
    """

    for num in numlist_odd: 
        diagonals[num] += numlist_odd
        reset += 1

        if math.sqrt(num) % 1 == 0 and reset == 4:
            dist += 2
            reset = 0

    return sum(diagonals)

print(spiralize(501, 15))