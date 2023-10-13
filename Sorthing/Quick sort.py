def Pivot(l, low, high):
    pivot = l[high]
    i = low-1
    for j in range(low, high-1):
        if l[j] <= pivot:
            i += 1
            l[i], l[j] = l[j], l[i]
    l[high], l[i+1] = l[i+1], l[high]
    return i+1

def Quick_Sort(l,low,high):
    if low<high:
        # for i in range(1000000): pass
        pivot_index = Pivot(l,low,high)
        print(l[low:high+1], low, high, pivot_index)
        Quick_Sort(l, low, pivot_index-1)
        Quick_Sort(l, pivot_index+1, high)

n = int(input())

if n==0:
    print(-1)

else:
    str = input().rstrip()
    l = str.split(' ')
    l = [eval(i) for i in l]

    if n==1:
        print(l[0])
    
    else:
        Quick_Sort(l, 0, len(l)-1)
        for i in l: print(i, end = ' ')

"""
# This function takes first element as pivot, the function
# places the pivot element(first element) on its sorted
# position and all the element lesser than pivot will placed
# left to it, and all the element greater than pivot placed
# right to it.
def partition(array, low, high):

	# First Element as pivot
	pivot = array[low]
	
	# st points to the starting of array
	start = low + 1
	
	# end points to the ending of the array
	end = high

	while True:
		# It indicates we have already moved all the elements to their correct side of the pivot
		while start <= end and array[end] >= pivot:
			end = end - 1

		# Opposite process
		while start <= end and array[start] <= pivot:
			start = start + 1

		# Case in which we will exit the loop
		if start <= end:
			array[start], array[end] = array[end], array[start]
			# The loop continues
		else:
			# We exit out of the loop
			break

	array[low], array[end] = array[end], array[low]
	# As we got pivot element index is end
	# now pivot element is at its sorted position
	# return pivot element index (end)
	return end

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index
def quick_sort(array, start, end):

	# If low is lesser than high
	if start < end:
	
		# idx is index of pivot element which is at its
		# sorted position
		idx = partition(array, start, end)
		
		# Separately sort elements before
		# partition and after partition
		quick_sort(array, start, idx-1)
		quick_sort(array, idx+1, end)

# Function to print an array
def print_arr(arr, n):
	for i in range(n):
		print(arr[i], end=" ")
	print()

# Driver Code
arr1 = [7, 6, 10, 5, 9, 2, 1, 15, 7]
quick_sort(arr1, 0, len(arr1)-1)
print_arr(arr1, len(arr1))

# This code is contributed by Aditya Sharma

"""