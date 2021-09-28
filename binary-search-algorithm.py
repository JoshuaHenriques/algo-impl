# Given a sorted array of n integers and a target value, determine if the target
# exists in the array in logarithmic time using the binary search algorithm
# (divide and conquer). If target exists in the array, print the index of it. 

# Input:
# nums[] = [1,4,5,7,8,9]
# target = 7
# Output: Element found at index 3

# linear search, checking each index sequentially, is O(n)

def binary_search(array, target, start, end):
	start = start
	end = len(array) - 1
	mid = (start + end) / 2
	if (target == array[mid]): return mid
	if (target < array[mid]): 
		binary_search(array, target, start, mid - 1)
	
	if (target > array[mid]): 
		binary_search(array, target, mid + 1, end)

def main():
	nums0 = [2,3,5,7,9]
	target0 = 7

	nums1 = [1,4,5,8,9]
	target1 = 2
	
if __name__ == '__main__':
    main()