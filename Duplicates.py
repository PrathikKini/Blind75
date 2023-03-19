def duplicates(nums):
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

print(duplicates([1,2,3,4,5,1]))