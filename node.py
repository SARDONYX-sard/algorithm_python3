# 二分探索用モジュール
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


def search(node, x):
    while node:
        if node.data == x:
            return True
        if x < node.data:
            node = node.left
        else:
            node = node.right
    return False


def insert(node, x):
    if node is None:
        return Node(x)
    elif x == node.data:
        return node
    elif x < node.data:
        node.left = insert(node.left, x)
    else:
        node.right = insert(node.right, x)
    return node


def search_min(node):
    if node.left is None: return node.data
    return search_min(node.left)


def delete_min(node):
    if node.left is None: return node.right
    node.left = delete_min(node.left)
    return node


def delete(node, x):
    if node:
        if x == node.data:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.data = search_min(node.right)
                node.right = delete_min(node.right)
        elif x < node.data:
            node.left = delete(node.left, x)
        else:
            node.right = delete(node.right, x)
        return node


def traverse_h(func, node):
    if node:
        traverse_h(func, node.left)
        func(node.data)
        traverse_h(func, node.right)


def traverse(node):
    if node:
        for x in traverse(node.left):
            yield x
        yield node.data
        for x in traverse(node.right):
            yield x


# 右回転
def rotate_right(node):
    lnode = node.left
    node.left = lnode.right
    lnode.right = node
    return lnode


# 左回転
def rotate_left(node):
    rnode = node.right
    node.right = rnode.left
    rnode.left = node
    return rnode
