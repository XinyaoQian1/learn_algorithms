"""
# @File    :    linked_list.py
# @Time    :    04/01/2023 15:19
# @Author  :    Xinyao Qian
# @SN      :    19021373
# @Description: 
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    # function: insert / delete / get / append
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, node):
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        self.size += 1

    def insert(self, node, index):
        # insert empty/ insert head/ insert tail/ insert middle
        # if 0 <= index <= self.size

        if self.size == 0:
            # empty
            self.append(node)
        elif index == 0:
            # head
            node.next, self.head = self.head, node
            self.size += 1
        elif index == self.size:
            # tail
            self.append(node)
            # self.tail.next = node
            # self.tail = node
        else:
            # middle
            pre = self.head
            for i in range(index-1):
                pre = pre.next
            node.next = pre.next
            pre.next = node

            self.size += 1

    def print(self):
        res = []
        node =  self.head
        while node:
            res.append(str(node.val))
            node = node.next
        res = '->'.join(res)
        print(res)


l = LinkedList()

l.append(ListNode())
l.append(ListNode(1))
l.append(ListNode(3))
l.insert(ListNode(2),2)
l.print()
print(l.size)

def reverse_list(head):
    curr = head
    pre = None
    while curr:
        next = curr.next

        curr.next = pre
        pre = curr

        curr = next
    return pre


def find_mid(head):
    # 还可以判断是否有环
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def sublist(head, left, right):
    curr = head
    for i in range(right):
        if i == left:
            head = curr
        curr = curr.next
    curr.next = None
    return head