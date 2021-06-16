# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def distributeCoins(self, root):
        self.ans = 0
        def dfs(node):
            if not node: 
                return 0
            L = dfs(node.left)
            R = dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + L + R - 1

        dfs(root)
        return self.ans
# 1. the node will go all the way to the left then goes either left or right until the bottom causing different layers becuase of line 13.
# 2. after line 12 returns an 0, it will go back a layer and contiune to run like 14.
# 3. the program will repeat step 1-2 to create layers becuase pf the recursive call line 14.
# 4. after another 0 returned, the node stop on the very bottom of the graph.
# 5. since now the node does not have left or right child, it will retun node.val + 0 + 0 - 1
# 6. after return node.val + 0 + 0 - 1, the program goes one layer up.
# 7. now L has a value (node.val + 0 + 0 - 1) and line 14 is excuted
# 8. same with previous steps, the node will goes to the right then goes either left or right until there is no child.
# 9. same steps keep repeating
# 10. finally, the value is retruned layer by layer until the root.

# 1. since we need all nodes have 1 coin, the one has 0 coin will be marked as -1 ( this is why we add -1 at line 16)
# 2. each recursive call, the coin needed or lacked until this node is being returned
# 4. by sum these numbers, we get the final answer
