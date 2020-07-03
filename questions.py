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


print(anagram("go go go", "gggooo"))
print(anagram("abc", "cba"))
print(anagram("hi man", "hi     man"))
print(anagram("aabbcd", "aabbc"))
print(anagram("123", "1 2"))
print("")
print(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))
print(pair_sum([1,2,3,1],3))
print(pair_sum([1,3,2,2],4))