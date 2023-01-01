"""
# @File    :    linkedlist.py
# @Time    :    31/05/2022 16:30
# @Author  :    Xinyao Qian
# @SN      :    19021373
# @Description: 
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
#
#
# def build_linkedlist():
#     # creat nodes
#     node_1 = ListNode(1)
#     node_2 = ListNode(3)
#     node_3 = ListNode(5)
#     node_4 = ListNode(7)
#
#     # assign their next
#     node_1.next = node_2
#     node_2.next = node_3
#     node_3.next = node_4
#
#     return node_1


# def run_linkedlist_example():
#     # creat nodes
#     node_1 = ListNode(1)
#     node_2 = ListNode(3)
#     node_3 = ListNode(5)
#     node_4 = ListNode(7)
#
#     # assign their next
#     node_1.next = node_2
#     node_2.next = node_3
#     node_3.next = node_4
#
#     # traverse
#     cur = node_1
#     while cur is not None:
#         print(cur.val)
#         cur = cur.next
#     print('\n')


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_empty(self,val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            return

    def insert_middle(self, location, val):
        # creat the node to be inserted
        new_node = ListNode(val)

        pre = self.head
        # insert in middle
        if location > 0:

            # from head move to the location-1

            for i in range(location - 1):
                pre = pre.next

            # connect the second half   new_node _> pre.next
            new_node.next = pre.next
            # connect the first half    pre -> new_node ->pre.next
            pre.next = new_node
            return

        # insert at front:
        elif location == 0:
            new_node.next = pre
            return

    def insert_end(self, val):
        new_node = ListNode(val)
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node
        return

    def remove_node(self,location):
        # in middle
        if location>0:
            pre = self.head
            for i in range(location-1):
                pre = pre.next
            pre.next = pre.next.next
        elif location == 0: # first node
            self.head = self.head.next

    def set_val(self,location,val):
        pre = self.head
        for i in range(location):
            pre = pre.next
        pre.val = val

    def print_node(self):
        # traverse
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next
        print('\n')


"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


def middle_node(self, head: ListNode) -> ListNode:
    # write your code here
    # 遍历链表得到长度：
    cur = head
    count = 1
    while cur.next is not None:
        count += 1
        cur = cur.next
    print(count // 2)




if __name__ == '__main__':
    # list = LinkedList()
    # list.insert_empty(1)
    # list.insert_end(2)
    # list.insert_end(4)
    # list.print_node()
    # list.insert_middle(2,3)
    # list.print_node()
    # list.set_val(1,3)
    # list.print_node()
    # list.remove_node(2)
    # list.print_node()





