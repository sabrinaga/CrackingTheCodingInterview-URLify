def urlify(inputString):
    arr = []
    prev = ""
    for i in inputString:

        if i != " ":
            arr.append(i)
            prev = i
        else:
            if prev != " ":
                arr.append("%20")
                prev = i
    return arr

def arrToString(arr):
    myString = ""
    
    for i in arr:
        myString += i

        # return string
    return myString


if __name__ == '__main__':

    text = "test text   with extra spaces   "
    solution = urlify(text)
    solutionString = arrToString(solution)
    print(arrToString(solutionString))
