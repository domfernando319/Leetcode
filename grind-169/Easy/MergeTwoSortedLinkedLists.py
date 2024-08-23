# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr1 = list1
        ptr2 = list2
        list3 = ListNode() #dummy node head for merged list
        ptr3 = list3

        # this loop will terminate if either one pointer reaches the end of their list
        while ptr1 and ptr2:
            #compare
            if ptr1.val <= ptr2.val:
                ptr3.next = ptr1
                ptr1 = ptr1.next
                
            else:
                ptr3.next = ptr2
                ptr2 = ptr2.next

            ptr3 = ptr3.next
                

        # At this point, one of the lists is exhausted. 
        # Attach the remaining part of the other list.
        if ptr1:
            # we know that rest of list1 must be appended to list3
            ptr3.next = ptr1
        elif ptr2 :
            ptr3.next = ptr2

        return list3.next




