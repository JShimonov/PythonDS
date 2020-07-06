import collections
import time

start_time = time.time()
# Q1
# create an anagram checker
def anagram(s1, s2):
    # change strings to not contain spaces or capitalizations
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # if len is different in the two then they are not anagrams
    if len(s1) != len(s2):
        return False
    
    # store values in dict
    dict1 = {}
    dict2 = {}

    # append all the chars into the dict
    for char in s1:
        if not char in dict1:
            dict1[char] = 1
        else:
            dict1[char] += 1

    # append all the chars from s2 into dict2
    for char in s2:
        if not char in dict2:
            dict2[char] = 1
        else:
            dict2[char] += 1

    # return
    if dict1 == dict2:
        return True
    return False

# Q2
# Array Pair Sum
# Description - Given an integer array, output all the unique pairs that sum up to a specific value k
def pair_sum(arr, k):
    # if there are less than 2 values, there is no tuple
    if len(arr) < 2:
        return

    # track values in arr
    seen = set()
    output = set()

    # iterate thru the arr
    for nums in arr:
        
        # check for complement value
        target = k - nums

        # check if complement value exists in seen
        if target not in seen:
            seen.add(nums)
        else:
            output.add( (min(nums, target), max(nums,target)) )

    return output

# Q3
# find the missing element
# description: consider an array of non-negative integers. A second array
# is formed by shuffling the elements of the first array and deleting a 
# random element. Given those two arrays, find which element is missing
# in the second array
def finder(arr1, arr2):
    
    # create a dict that add values from arr2
    arr = collections.defaultdict(int)

    for num in arr2:
        arr[num] += 1
    
    for num in arr1:
        if arr[num] == 0:
            return num
        else:
            arr[num] -= 1

def cleverFinder(arr1, arr2):
    result = 0

    # perform XOR between the numbers in the arrays
    for num in arr1+arr2:
        result ^= num
    return result

# Q4
# largest Continuous Sum
# Description: Given an array of integers (positive and negative) find
# the largest continuous sum
def large_cont_sum(arr):

    if len(arr) == 0:
        return 0
    
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum+num, num)

        max_sum = max(current_sum, max_sum)
    return max_sum


#Q1
print(anagram("go go go", "gggooo"))
print(anagram("abc", "cba"))
print(anagram("hi man", "hi     man"))
print(anagram("aabbcd", "aabbc"))
print(anagram("123", "1 2"))
print("--- %s seconds ---" % (time.time() - start_time))
#Q2
print(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))
print(pair_sum([1,2,3,1],3))
print(pair_sum([1,3,2,2],4))
print("--- %s seconds ---" % (time.time() - start_time))
#Q3
arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
print(finder(arr1,arr2))
arr1 = [5,5,7,7]
arr2 = [5,7,7]
print(finder(arr1,arr2))
print("--- %s seconds ---" % (time.time() - start_time))
print(large_cont_sum([1,2,-1,3,4]))
print("--- %s seconds ---" % (time.time() - start_time))
