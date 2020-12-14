# tree

+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
+ [Invert Binary Tree](#invert-binary-tree)
+ [Binary Tree Level Order Traversal](binary_tree_level_order_traversal)
+ [Kth Smallest Element in a BST](kth-smallest-element-in-a-bst)

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

## Invert Binary Tree


https://leetcode.com/problems/invert-binary-tree/


```python
def invert(self, node):
    if node is None:
        return 
    node.left, node.right = node.right, node.left
    self.invert(node.left)
    self.invert(node.right)
    
def invertTree(self, root: TreeNode) -> TreeNode:
    self.invert(root)
    return root
```

## Binary Tree Level Order Traversal


https://leetcode.com/problems/binary-tree-level-order-traversal/

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
        
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    res = []
    self.BFS(root, res, 1)
    return res
```

## Kth Smallest Element in a BST


https://leetcode.com/problems/kth-smallest-element-in-a-bst/

```python
def collect(self, node, order):
    order.append(node.val)
    if node.left is not None:
        self.collect( node.left, order)
    if node.right is not None:
        self.collect( node.right, order)
   
def kthSmallest(self, root: TreeNode, k: int) -> int:
    order = []
    self.collect(root, order)
    order.sort()
    return order[k-1]
```