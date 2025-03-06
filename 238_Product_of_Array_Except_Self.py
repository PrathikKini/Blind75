def productExceptSelf(nums):
    prefix = postfix = 1
    res = [1] * len(nums)

    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    for i in range(len(nums)-1,-1,-1):
        res[i] *= postfix
        postfix *= nums[i]

    return res

print(productExceptSelf([1,2,4,6]))
print(productExceptSelf([-1,1,0,-3,3]))
