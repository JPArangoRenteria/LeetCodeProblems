# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        L1 = []
        L2 = []
        while l1 is not None:
            L1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            L2.append(l2.val)
            l2 = l2.next
        rev1 = L1[::-1]
        rev2 = L2[::-1]
        n1 = ''
        n2 = ''
        for i in range(0,len(rev1)):
            n1 = n1 + str(rev1[i])
        for j in range(0,len(rev2)):
            n2 = n2+str(rev2[j])
        m = str(int(n1)+int(n2))[::-1]
        dummy_head = ListNode(0)
        curr = dummy_head
        for k in range(0,len(m)):
            new_node = ListNode(int(m[k]))
            curr.next = new_node
            curr = new_node
        return dummy_head.next

        
