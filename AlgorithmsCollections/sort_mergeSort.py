import random
"""
Average Time complexity: O(n*log(n))
Best Time complexity: O(n*log(n))
"""
def mergeSort(array):
    if len(array) == 1:
        return array

    firstHalf = array[:len(array)//2]
    secondHalf = array[len(array)//2:]
    firstHalf = mergeSort(firstHalf)
    secondHalf = mergeSort(secondHalf)

    final = []
    i,j = 0,0
    while i<len(firstHalf) and j<len(secondHalf):  ###########merge the two sorted array
        if firstHalf[i] <= secondHalf[j]:
            final.append(firstHalf[i])
            i+=1
        else:
            final.append(secondHalf[j])
            j+=1
    left = secondHalf[j:] if i==len(firstHalf) else firstHalf[i:]
    return final + left

