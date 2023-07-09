import numpy as np
import time

def countingSort(inputArray):
    # Find the maximum element in the inputArray
    maxElement= max(inputArray)

    countArrayLength = maxElement+1

    # Initialize the countArray with (max+1) zeros
    countArray = [0] * countArrayLength

    # Step 1 -> Traverse the inputArray and increase 
    # the corresponding count for every element by 1
    for el in inputArray: 
        countArray[el] += 1

    # Step 2 -> For each element in the countArray, 
    # sum up its value with the value of the previous 
    # element, and then store that value 
    # as the value of the current element
    for i in range(1, countArrayLength):
        countArray[i] += countArray[i-1] 

    # Step 3 -> Calculate element position
    # based on the countArray values
    outputArray = [0] * len(inputArray)
    i = len(inputArray) - 1
    while i >= 0:
        currentEl = inputArray[i]
        countArray[currentEl] -= 1
        newPosition = countArray[currentEl]
        outputArray[newPosition] = currentEl
        i -= 1

    return outputArray

# arq_name = str(i)+'.txt'
arq_name = '1.txt'
s_time = time.time()
arquivo = np.loadtxt('../Arquivos_Entrada/1.txt', dtype=float)
e_time = time.time()
print(e_time - s_time)
print(arquivo)
# ordlin = np.sort(a, axis=1)
# ordcol = np.sort(a, axis=0)

# inputArray = [2,2,0,6,1,9,9,7]
# print("Input array = ", inputArray)

# sortedArray = countingSort(inputArray)
# print("Counting sort result = ", sortedArray)