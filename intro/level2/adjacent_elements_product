#
# https://app.codesignal.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m
#

def adjacentElementsProduct(inputArray):
    product = -32768
    for i in range(0, len(inputArray)-1):
        if inputArray[i] * inputArray[i+1] > product:
            product = inputArray[i] * inputArray[i+1]
    return product


print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))