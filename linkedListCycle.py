from listNode import ListNode
'''
Prompt:
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
'''

def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head == None:
        return False
    slow = head
    fast = head
    while fast.next != None:
        slow = slow.next
        fast = fast.next
        if fast.next == None:
            break
        fast = fast.next
        if slow == fast:
            return True
    return False

if __name__ == "__main__":
    head = ListNode(3)
    next = ListNode(2)
    head.next = next
    next2 = ListNode(0)
    next.next = next2
    next = ListNode(-4)
    next2.next = next
    next.next = head.next
    print(hasCycle(head))