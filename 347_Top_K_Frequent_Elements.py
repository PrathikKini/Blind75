# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
 
def topKfrequentelement(nums,k):
    count = {}
    res = []
    freq = [[] for i in range(len(nums)+1)]

    for num in nums:
        count[num] = 1 + count.get(num,0)

    for num,cnt in count.items():
        freq[cnt].append(num)

    for i in range(len(freq)-1,0,-1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res        

print(topKfrequentelement([1,1,1,2,2,3],2))
print(topKfrequentelement([1],1))
