from listNode import ListNode
'''
Prompt:
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
'''
def swapPairs(head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None:
            return
        cur = head
        prev = None
        nxt = head.next
        nxt2 = None
        while cur != None:
            if nxt != None: 
                if prev != None:
                    prev.next = nxt
                else: # prev == None
                    head = nxt
            nxt2 = nxt.next if nxt!=None else None
            if nxt!=None:
                nxt.next = cur 
            cur.next = nxt2
            prev = cur
            cur = nxt2
            if cur == None:
                break
            nxt = cur.next
        return head

if __name__ == "__main__":
    head = ListNode(3)
    next = ListNode(2)
    head.next = next
    next2 = ListNode(0)
    next.next = next2
    next = ListNode(-4)
    next2.next = next
    head = swapPairs(head)
    cur = head
    while cur!=None:
        print(cur.val)
        cur = cur.next