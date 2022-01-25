"""
Function that determines if two inputs are permutations of one another
Args:
    param1: The first input value
    param2: The second input value
Returns:
    Returns true if the inputs are permutations of one another. Returns false otherwise.
"""

def arePermutation(x, y):
    #if the inputs are not of the same length then they can not be permutations
    if len(x) != len(y):
        return False
    #if the inputs are empty then there are no permutations
    if len(x) == 0 or len(y) == 0:
        return False
    
    x_sorted = sorted(x)
    y_sorted = sorted(y)

    x_string = "".join(x_sorted)
    y_string = "".join(y_sorted)
 
    for i in range(0,len(x),1):
        if (x_string[i] != y_string[i]):
            return False
    return True

"""
Function that returns all the possible permutations of a given input
Args:
    param1: The input string which we want permutations for
Returns:
    Returns the possible permutations as a list
"""

def possiblePermuations(x):
    permutation_list = []
    #if the length is 0 there is nothign to rearange return an empty list
    if len(x) == 0:
        return []
    #if the length is 1 then there is nothing to rearange, return the list with original input 
    if len(x) == 1:
        return [x]
    for i in range(len(x)):
        head = x[i]
        remaining_x = x[:i] + x[i+1:]
        for j in possiblePermuations(remaining_x):
            permutation_list.append([head] + j)
    return permutation_list




if __name__ == '__main__':
    a = list("cat")
    answer = possiblePermuations(a)
    print("Total possible permuations:", len(answer))
    for x in range(len(answer)):
        print(answer[x],)

    b = "nest"
    c = "test"
    d = "max"
    e = "xma"

    answer2 = arePermutation(c, b)
    print("Answer2: ", answer2)

    answer3 = arePermutation(d,e)
    print("Answer3:", answer3)
