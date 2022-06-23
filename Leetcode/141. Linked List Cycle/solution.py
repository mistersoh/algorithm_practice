# Why & How?

'''
Create Fast and slow pointer, which initially are head.
When only there exist fast, fast.next and fast.next.next get next linked list 
value for slow and fast pointer. If the linked list has cycle in it, both slow and fast
meets one day, returns True, else return False
'''

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                return True
            
        return False

# Better version (Runtime: 44 ms, faster than 92.24%, Memory Usage: 20.6 MB, less than 26.94%)

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

# Learnt something new
'''
The "trick" is to not check all the time whether we have reached the end but to handle it via an exception. "Easier to ask for forgiveness than permission."
'''