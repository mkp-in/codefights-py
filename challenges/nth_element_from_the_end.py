# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x, next=None):
    self.value = x
    self.next = next

def nthElementFromTheEnd(l, n):
    curr = l
    if curr.next is None and n > 0:
        return -1
    for i in range(n):
        if curr is None:
            return -1
        curr = curr.next

    p = l
    while curr is not None:
        p = p.next
        curr = curr.next

    return p.value


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(nthElementFromTheEnd(head, 2))