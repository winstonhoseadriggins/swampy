import random
from collections import deque

class Tree(object):
    def __init__(self, cargo=None, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def add(self, cargo):
        attr = random.choice(['left', 'right'])
        tree = getattr(self, attr)
        if tree == None:
            setattr(self, attr, Tree(cargo))
        else:
            tree.add(cargo)

    def __str__(self):
        t = []
        queue = deque([self])

        while queue:
            tree = queue.popleft()
            if tree == None: 
                t.append('X')
            else:
                t.append(str(tree.cargo))
                queue.extend([tree.left, tree.right])
                
        return ', '.join(t)


def flip_tree(tree):
    if tree == None:
        return None

    return Tree(tree.cargo, flip_tree(tree.right), flip_tree(tree.left))

tree = Tree(1)
for i in range(2,8):
    tree.add(i)

print tree
tree2 = flip_tree(tree)
print tree2
