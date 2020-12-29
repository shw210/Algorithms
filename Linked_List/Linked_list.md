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
        """
        :type head: ListNode
        :rtype: ListNode
        """
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
        """
        :type head: ListNode
        :rtype: ListNode
        """
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
