# Why & How?
'''
We need two linked list in order to get kth value from start and end.
We first copy head (call this 'n'), move to kth from start, copy this again call this as 'a'.
We then copy original linked list again (call this 'b'), and start move both 'n' and 'b' 
to the end until 'n' reaches to the end.
This works since 'n' already moved to the kth value, when it reaches to the end the remaining
values 'b' get until the end point equals to k, which is the kth value from the end.
We finally swap the current value of 'a' and 'b' and returns head.
'''

class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        n  =  head
        for _ in range(k-1):
            n  =  n.next
        
        a  =  n
        b  =  head
        
        while n.next:
            b  =  b.next
            n  =  n.next
        
        a.val, b.val  =  b.val, a.val
        
        return head

# Learnt something new
'''
'''