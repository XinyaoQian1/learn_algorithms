"""
# @File    :    binary_tree.py
# @Time    :    18/06/2022 14:44
# @Author  :    Xinyao Qian
# @SN      :    19021373
# @Description: 
"""
from queue import Queue

class TreeNode:

    # 基本属性
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree():
    # 先构建单个的节点：
    node1 = TreeNode(3)
    node2 = TreeNode(4)
    node3 = TreeNode(5)
    node4 = TreeNode(6)
    node5 = TreeNode(7)
    node6 = TreeNode(8)

    # 给左右进行赋值(连接）
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6

    return node1

def traverse_tree(root):
    print(root.val,end='')
    traverse_tree(root.left)
    traverse_tree(root.right)




def breadth_first_traverse(root):#宽度优先遍历
    if not root:
        return -1

    que=Queue
    que.put(root)

    while not que.empty():
        #获取了宽度：
        width= que.size()

        for i in range(width):#取出该level的值
            cur = que.get()#取出
            print(cur.val,end='')
            if cur.left:
                que.put(cur.left)
            if cur.right:
                que.put(cur.right)







if __name__ == '__main__':
    root = build_tree()
    traverse_tree(root)