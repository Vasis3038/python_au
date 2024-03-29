# linked-list

+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-Linked-List)
+ [Palindrome Linked List](#palindrome-linked-list)
+ [Merge Two Sorted Lists](#merge-two-sorted-lists)
+ [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)
+ [Linked List Cycle II](#linked-list-cycle-II)
+ [Linked List Cycle](#linked-list-cycle)
+ [Reorder List](#reorder-list)
+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)
+ [Sort List](#sort-list)
+ [Merge k Sorted Lists](#merge-k-sorted-lists)

## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

```python
def reverseList(self, head: ListNode) -> ListNode:
    cur = head
    Next = None
    prev = None
    while cur != None:
        Next = cur.next
        cur.next = prev
        prev = cur
        cur = Next
    return prev  
```
## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

```python
def middleNode(self, head: ListNode) -> ListNode:
    one = head
    two = head
    while (two != None) and (two.next != None):
        one = one.next
        if two.next == None:
            two = two.next
        else:
            two = two.next.next
    return one
```

## Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

```python
def isPalindrome(self, head: ListNode) -> bool:
    one = head
    two = head
    while (two != None) and (two.next != None):
        one = one.next
        if two.next == None:
            two = two.next
        else:
            two = two.next.next
    n = 0;
    sch = head;
    while sch != None:
        n = n + 1
        sch = sch.next
    if n%2 != 0:
        one = one.next
    cur = one
    Next = None
    prev = None
    while cur != None:
        Next = cur.next
        cur.next = prev
        prev = cur
        cur = Next
    one = prev
    flag = 1
    while one != None:
        if head.val != one.val:
            flag = 0
        head = head.next
        one = one.next
    return flag
```

## Merge Two Sorted Lists


https://leetcode.com/problems/merge-two-sorted-lists/

```python
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    sorted_list = ListNode()
    cur = sorted_list    
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next       
    if l1 is None:
        cur.next = l2
    if l2 is None:
        cur.next = l1   
    return sorted_list.next
```

## Remove Nth Node From End of List


https://leetcode.com/problems/remove-nth-node-from-end-of-list/

```python
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    cur = head
    sch = 0
    while cur is not None:
        sch += 1
        cur = cur.next            
    cur = head
    if cur.next is None:
        return None        
    for i in range(n):
        if cur.next is not None:
            cur = cur.next         
    cur2 = head.next
    prev = head
    while cur.next is not None:
        cur = cur.next
        cur2 = cur2.next
        prev = prev.next
    prev.next = prev.next.next
    if sch is n:
        return cur2
    return head    
```

## Linked List Cycle II


https://leetcode.com/problems/linked-list-cycle-ii/

```python
def detectCycle(self, head: ListNode) -> ListNode:
    s = head
    f = head
    while f and f.next:
        f = f.next.next
        s = s.next
        if f == s:
            f = head
            while f is not s:
                f = f.next
                s = s.next
            return s
    return None  
```

## Linked List Cycle


https://leetcode.com/problems/linked-list-cycle/

```python
def hasCycle(self, head: ListNode) -> bool:
    s = head
    f = head
    while f and f.next:
        f = f.next.next
        s = s.next
        if f == s:
            return 1
    return 0
```

## Reorder List


https://leetcode.com/problems/reorder-list/

```python
def get_middle_of_list(self, head):
    if head is None or head.next is None:
        return
    one = head
    two = head
    while (two != None) and (two.next != None):
        one = one.next
        if two.next == None:
            two = two.next
        else:
            two = two.next.next
    p = head
    while p.next is not one:
        p = p.next
    p.next = None
    return one
    
def reverse_list(self, head):
    cur = head
    Next = None
    prev = None
    while cur != None:
        Next = cur.next
        cur.next = prev
        prev = cur
        cur = Next
    return prev 
 
def reorderList(self, head: ListNode) -> None:
    head3 = head
    cur = ListNode()
    if head is None or head.next is None:
        return
    if head.next.next is None:
        return
    if head.next.next.next is None:
        cur = head.next
        head.next = head.next.next
        head.next.next = cur
        cur.next = None
        return
    head2 = self.get_middle_of_list(head)
    head2 = self.reverse_list(head2)
    cur2 = ListNode()
    while(head.next != None and head2.next != None):
        cur = head.next
        head.next = head2
        cur2 = head2.next
        head.next.next = cur
        head = head.next.next
        head2 = cur2
    head.next = cur2
    return head3
```

## Intersection of Two Linked Lists


https://leetcode.com/problems/intersection-of-two-linked-lists/

```python
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    cura = headA
    curb = headB
    lena = 0
    lenb = 0
    while cura != None:
        lena += 1
        cura = cura.next
    while curb != None:
        lenb += 1  
        curb = curb.next
    if lena > lenb:
        cura = headB
        curb = headA
        a = lena
        lena = lenb
        lenb = a
    else:
        cura = headA
        curb = headB
    while lenb != lena:
        curb = curb.next
        lenb -= 1
    while curb != cura:
        if cura is None:
            return 0
        cura = cura.next
        curb = curb.next
    return cura
```

## Sort List


https://leetcode.com/problems/sort-list/

```python
def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not l1: 
        return l2
   if not l2: 
        return l1
    if l1.val < l2.val:
        left, right = l1, l2 
    else:
        left, right = l2, l1
    res = left
    while left.next and right:
        if right.val < left.next.val:
            temp = right.next
            right.next = left.next
            left.next = right
            right = temp
        left = left.next    
    if right:
        left.next = right
    return res

def sortList(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    p, s, f = None, head, head
    while f and f.next:
            p = s
            s = s.next
            f = f.next.next
    p.next = None
    return self.merge(self.sortList(head), self.sortList(s))
```

## Merge k Sorted Lists


https://leetcode.com/problems/merge-k-sorted-lists/

```python
def mergeKLists(self, lists):
	lst = []
	for i in lists:
		while i:
			lst.append(i.val)
			i = i.next
	lst.sort()
	head = ListNode()
	tmp = head
	for i in range(0,len(lst)):
		tmp.next = ListNode(lst[i])
		tmp = tmp.next
	return head.next
```