# linked-list

+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-Linked-List)
+ [Palindrome Linked List](#palindrome-linked-list)
+ [Merge Two Sorted Lists](#merge-two-sorted-lists)

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
    if(l1.val > l2.val): #здесь я сделал совершенно гениальный ход! чтобы не рассматривать доп случай, я "приравнял" его к уже разобранному  
        t = l1
        l1 = l2
        l2 = t
    a = l2
    prev1 = l1 #prev1 и prev2 - сравниваемые элементы списков  
    prev2 = l2
    a = l1 #a - первый элемент списка, который мы соединяем
    n = 0 #счетчик n нужен, чтобы понять, в первый или нет раз, рассматриваются списки, если в первый, то подход нужен особенный
    while (prev1 != None) and (prev2 != None):
        if (prev1.val == prev2.val): 
            if(n == 0):
                prev1 = l1.next
                l1.next = prev2
                l1 = l1.next 
                prev2 = prev2.next
            else:
                l1.next = prev2
                l1 = l1.next
                prev2 = prev2.next
                l1.next = prev1
                l1 = l1.next                    
                prev1 = prev1.next           
        else:
            if (prev1.val < prev2.val):
                if(n != 0):
                    l1.next = prev1
                    l1 = l1.next
                    prev1 = prev1.next
                        
                else:
                    prev1 = prev1.next    
            else:
                if (prev2.val < prev1.val): 
                        l1.next = prev2
                        l1 = l1.next
                        prev2 = prev2.next 
                            
        if (prev1 == None and prev2 != None): 
            l1.next = prev2
            l1 = l1.next
            prev2 = None
                
        if (prev2 == None and prev1 != None):
            l1.next = prev1
            l1 = l1.next
            prev1 = None
        n = n+1  
    return a
```
