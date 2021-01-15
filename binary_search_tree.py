import node
from elapsed_time import elapsed_time

# 二分探索木
class BinaryTree:
    def __init__(self):
        self.root = None

    # 探索
    def search(self, x):
        return node.search(self.root, x)

    # 挿入
    def insert(self, x):
        self.root = node.insert(self.root, x)

    # 削除
    def delete(self, x):
        self.root = node.delete(self.root, x)

    # 巡回
    def traverse(self):
        for x in node.traverse(self.root):
            yield x

    def __str__(self):
        if self.root is None:
            return 'BinaryTree()'
        buff = 'BinaryTree('
        for x in node.traverse(self.root):
            buff += '%s, ' % x
        buff = buff.rstrip(', ')
        buff += ')'
        return buff


@elapsed_time
def main():
    import random
    tree = BinaryTree()
    data = [random.randint(0, 100) for _ in range(10)]
    print(data)
    print(tree)
    for x in data:
        tree.insert(x)
    print('tree')
    for x in data:
        print('search', x, tree.search(x))
        print('delete', x)
        tree.delete(x)
        print('search', x, tree.search(x))
        print(tree)


if __name__ == '__main__':
    main()
