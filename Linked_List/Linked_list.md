## 83. Remove Duplicates from Sorted List
```Python
class Solution(object):
    def deleteDuplicates(self, head):
       current = head 
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
                
        return head
```
## 19. Remove Nth Node From End of List
思路：因为linked list不容易知道它的size，所以我们必须用 two pointer 的方法找到倒数第 n 个 node 是哪个       
注意：1. 不要return head, 因为 head 本身也有可能是那个被去除的Node 2. 注意dummy node的用法

```Python
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(val = 0, next = head)
        fast = slow = dummy
        
        i = 0
        while i <= n:
            fast = fast.next
            i += 1
            
        while fast:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return dummy.next

```
## 24. Swap Nodes in Pairs (Medium)
写法一：注意的就是在写 while function的时候，先确保满足条件然后再赋值； 以及创建dummy node 作为第一个 pre node 的做法

```Python
class Solution(object):
    def swapPairs(self, head):
       
        if head is None: return None
        
        pre = dummy = ListNode(next = head)
        
        while pre and pre.next and pre.next.next: #先确保满足条件
            #然后再赋值
            slow = pre.next
            fast = pre.next.next 
            
            #然后再调整Pointer的指向
            slow.next = slow.next.next
            fast.next = slow
            pre.next = fast
            
            #然后更新pre的位置
            pre = pre.next.next
            
            
        return dummy.next
```


写法二：写一个swap function， pre.next and pre.next.next 都有值，然后call swap function， 这种写法更简洁
```Python
class Solution(object):
    def swapPairs(self, head):
       
        dummy = pre = ListNode(next = head)
        
        while pre and pre.next and pre.next.next:
            self.swap(pre)
            pre = pre.next.next
        
        return dummy.next
    
    def swap(self, pre):
            slow = pre.next
            fast = pre.next.next 
            
            slow.next = slow.next.next
            fast.next = slow
            pre.next = fast

```
## 445. Add Two Numbers II
思路：将两个list放入stack中，然后pop并且计算，然后创建结果linked list. 注意两数相加，loop结束后要对 carry 做最后的处理

```Python
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        stack1, stack2 = [l1.val], [l2.val]
        
        current = l1
        while current.next:
            stack1.append(current.next.val)
            current = current.next
        
        current = l2
        while current.next:
            stack2.append(current.next.val)
            current = current.next
        
        carry = 0
        pre = None
        while stack1 or stack2:
            added = carry
            if stack1:
                added += stack1.pop()
            if stack2:
                added += stack2.pop()
                
            carry = added // 10
            num = added % 10
            
            new_node = ListNode(val = num, next = pre)
            pre = new_node
            
        if carry:
            new_node = ListNode(val = carry, next = pre)
            
        return new_node
```

## 725. Split Linked List in Parts
注意：  
1. result = [None for i in range(k)] 的写法        
2. 使用两个指针，一个用来加 head node, 一个用来切断每一节的最后一个node
```Python
class Solution(object):
    def splitListToParts(self, root, k):
        
        #计算长度
        head = root
        ttl_len = 0
        while head:
            ttl_len += 1
            head = head.next
        
        avg, longer  = ttl_len // k, ttl_len % k
        
        result = [None for i in range(k)]
        
        if not root: return result
        
        # create answer
        cnt = 0
        pre, head = None, root
        for i in range(k):
            result[i] = head
            for l in range(avg + max(0, longer > 0)):
                pre = head
                head = head.next
            pre.next = None
            longer -= 1
            
        return result
```
