# tree

+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
+ [Invert Binary Tree](#invert-binary-tree)
+ [Binary Tree Level Order Traversal](#binary_tree_level_order_traversal)
+ [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)
+ [Validate Binary Search Tree](#validate-binary-search-tree)
+ [Symmetric Tree](#symmetric-tree)
+ [Binary Search Tree Iterator](#binary-search-tree-iterator)

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

## Validate Binary Search Tree


https://leetcode.com/problems/validate-binary-search-tree/

```python
def check(self, node, l, r):
    if node is None:
        return 1
    if l < node.val < r:  
        return self.check(node.left, l, node.val) * self.check(node.right, node.val, r)
    return 0
        
def isValidBST(self, root: TreeNode, l = float('-inf'), r = float('inf')):
    return self.check(root, -inf, +inf)
```

## Symmetric Tree


https://leetcode.com/problems/symmetric-tree/

```python
def check(self, node, node2):
    if node is None and node2 is None:
        return 1
    if node is not None and node2 is not None:
        if node.val == node2.val:
            return(self.check(node.left, node2.right) * self.check(node.right, node2.left))
    return 0
        
def isSymmetric(self, root: TreeNode):
    return self.check(root, root)
```

## Binary Search Tree Iterator


https://leetcode.com/problems/binary-search-tree-iterator/

```python
def __init__(self, root: TreeNode):
    self.root = root
    self.ord = []
    node = root
    while node:
        self.ord.append(node)
        node = node.left
        
def next(self) -> int:
    node = self.ord.pop()
    if node.right is not None:
        self.ord.append(node.right)
        curr = self.ord[-1]
        while curr.left is not None:
            self.ord.append(curr.left)
            curr = curr.left
    return node.val        
        
def hasNext(self) -> bool:
    return len(self.ord) != 0 
```
