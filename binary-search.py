def binary_search_recursion(array, target, left, right):
	if left > right:
		return -1
	mid = (right + left) // 2
	if target == array[mid]: 
		return mid
	elif target < array[mid]: 
		return binary_search_recursion(array, target, left, mid - 1)
	else: 
		return binary_search_recursion(array, target, mid + 1, right)

def binary_search_iterative(array, target):
	(left, right) = (0, len(array) - 1)
	while left <= right:
		mid = (right + left) // 2
		if target == array[mid]:
			return mid
		elif target < array[mid]:
			right = mid - 1
		else:
			left = mid + 1
	return -1

def main():
	print(f'Binary Search Algorithm: ')
	
	nums0 = [2,5,6,8,9,10]
	(left, right) = (0, len(nums0) - 1)
	target0 = 9
	print(f'recursive: {binary_search_recursion(nums0, target0, left, right)}')
	
	nums1 = [1,4,5,8,9]
	target1 = 9
	print(f'iterative: {binary_search_iterative(nums1, target1)}')
	
if __name__ == '__main__':
    main()