# tree

+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)

## Maximum Depth of Binary Tree


https://leetcode.com/problems/maximum-depth-of-binary-tree/

```python
def BFS(self, node, res, floor):
    if node is None:
        return
    if floor > len(res):
        res.append([])
    res[floor-1].append(node.val)
    self.BFS(node.left, res, floor + 1)
    self.BFS(node.right, res, floor + 1)
    return res
           
def maxDepth(self, root: TreeNode) -> List[List[int]]:
    res = []
    self.BFS(root, res, 1)
    return len(res)
```

## Binary Tree Inorder Traversal


https://leetcode.com/problems/binary-tree-inorder-traversal/

```python
def inorder(self, node, order):
    if node is None:
        return
    self.inorder(node.left, order)
    order.append(node.val)
    self.inorder(node.right, order)
             
def inorderTraversal(self, root: TreeNode) -> List[int]:
    order = []
    self.inorder(root, order)
    return order
```