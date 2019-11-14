def bubbleSort(array):
    for i in range(len(array)):
        
        arrLeft = len(array)-i-1
        for j in range(0, arrLeft):

            if array[j] > array[j + 1]:
                (array[j], array[j + 1]) = (array[j + 1], array[j])
                
                
data = [-2, 45, 0, 11, -9]
bubbleSort(data)
print('Sorted Array in Ascending Order:')
print(data)