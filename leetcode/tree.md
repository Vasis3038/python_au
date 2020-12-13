# tree

+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)

## Maximum Depth of Binary Tree


https://leetcode.com/problems/maximum-depth-of-binary-tree/

```python
def maxDepth(self, root: TreeNode) -> List[List[int]]:
    if root is None:
        return 0
    return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
```