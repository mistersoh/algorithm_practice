# Why & How?

'''
Scanning both list1 and list2, compare each current values 
until one list node ends. Put rest of values in relatively longer list node (since these
values are larger than other list node's values it does not need further sorting)

Return next values in result list node so skip first value (which is 0) by ListNode(0)
'''

current = res = ListNode(0) # Declare dummy list nodes
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next
            
        current.next = list1 or list2
            
        return res.next

# Learnt something new
'''
current = res = ListNode(0)

Since both dummy list node current and res, when one gets value change, it affects to the other
'''