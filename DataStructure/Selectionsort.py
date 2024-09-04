def selectionsort(array,size):
    for ind in range(size):
        min_index=ind
        for j in range(ind+1,size):
            if array[j]<array[min_index]:
                min_index=j
        (array[ind],array[min_index])=(array[min_index],array[ind])
arr=list(map(int,input("Enter the elements separated with spaces : ").split()))
size=len(arr)
selectionsort(arr,size)
print("The array after sorting in Ascending order by selection sort is:")
print(arr)
