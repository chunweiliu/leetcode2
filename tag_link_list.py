# Tag: Link list

class ListNode():
    def __init__(self, val, nxt=None):
        self.value = val
        self.next = nxt


def reverse(head):
    prev, curr = None, head

    while curr:
        next = curr.next
        curr.next = prev

        prev = curr
        curr = next
    return prev

def reverse_pair(head):
    """
    prev -> a -> b -> b.next
    prev -> b -> a -> b.next
    """
    dummy = ListNode(0)
    prev, prev.next = dummy, head

    while prev.next and prev.next.next:
        a = prev.next
        b = prev.next.next

        prev.next, a.next, b.next = b, b.next, a

        # bug
        prev = a
    return dummy.next


