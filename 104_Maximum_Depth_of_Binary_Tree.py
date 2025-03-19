# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

def maxdepth(root):
    # if not root:
    #     return 0
    # return 1 + max(maxdepth(root.left),maxdepth(root.right))
    # or
    q = deque()
    if root:
        q.append(root)

    level = 0
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level