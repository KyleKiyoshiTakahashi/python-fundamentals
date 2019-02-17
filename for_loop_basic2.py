# Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". 
# Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].

def biggie_size(arr):
	for i in range(len(arr)):
		if arr[i] > 0:
			arr[i] == "big"
	return arr

# Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. 
# Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  
# (Note that zero is not considered to be a positive number).

def count_pos(arr):
	count = 0
	for i in range(len(arr)):
		if arr[i] > 0:
			count ++
	count = arr[len(arr)-1]
	arr = arr.append(count)
	return arr

# SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  
# For example sumTotal([1,2,3,4]) should return 10

def sum_total(arr):
	sum = 0
	for i in range(len(arr)):
		sum = sum + arr[i]
	return sum

# Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  
# For example multiples([1,2,3,4]) should return 2.5

def get_average(arr):
	sum = 0
	for i in range(len(arr)):
		sum = sum + arr[i]
	return sum/len(arr)

# Length - Create a function that takes an array as an argument and returns the length of the array.  
# For example length([1,2,3,4]) should return 4

def arr_length(arr):
	return len(arr)

# Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  
# If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; 
# minimum([-1,-2,-3]) should return -3.

def min_val(arr):
	min = arr[0]
	if len(arr) == 0:
		return False
	for i in range(len(arr)):
		if arr[i] < min:
			arr[i] = min
	return min

# Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  
# If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; 
# maximum([-1,-2,-3]) should return -1.

def max_array(arr):
	max = arr[0]
	if len(arr) == 0:
		return False
	for i in range(len(arr)):
		if arr[i] > max:
			arr[i] = max
	return max

print(max_array([]))

# UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the 
# sumTotal, average, minimum, maximum and length of the array.

def ultimate_analyze(arr):
	sum_total = 0
	min = arr[0]
	max = arr[0]
	for i in range(1, len(arr)):
		if arr[i] > max:
			max = arr[i]
		if arr[i] < min:
			min = arr[i]
		sum_total = sum_total + arr[i]
	avg = sum_total / len(arr)
	new_dictionary = {
		"maximun": max,
		"minimum": min,
		"sum_total": sum_total,
		"average": avg,
		"length": len(arr)
	}
	return new_dictionary
print(ultimate_analyze([1,2,3,4,5]))
# ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  
# Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. 
# This challenge is known to appear during basic technical interviews.

def reverse_list(arr):
new_arr = arr[::-1]
print(new_arr)

print(reverse_list([1,2,3,4]))

def reverse_list(arr):
  for i in range(int(len(arr)/2)):
    temp = arr[i]
    arr[i]= arr[len(arr)-1-i]
    arr[len(arr)-1-i] = temp
  return arr

print(reverse_list([1,2,3,4]))


