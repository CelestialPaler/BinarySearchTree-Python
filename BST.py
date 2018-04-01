
# Node for BST
class Node:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return "Node({})".format(self.key)

    def __str__(self):
        return "A node of a BST."

# Binary Search Tree Class
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def random_fill(self, key_number):
        from random import random
        data_set = set()
        data_range = 1000 # 1e
        while len(data_set) < key_number:
            temp = (int)(random() * data_range)
            data_set.add(temp)
            self.insert(temp)

    # insert function
    def insert(self, new_key):
        if self.root is None:
            self.root = Node(new_key)
        else:
            self._insert(self.root, new_key)

    # search function
    def search(self, tar_key):
        if self.root is None:
            return False
        else:
            return self._search(self.root, tar_key)

    # preorder traversing function
    def traverse_pre_order(self):
        result = list()
        if self.root is not None:
            self._traverse_pre_order(self.root, result)
        else:
            pass
        print(result)

    # inorder traversing function
    def traverse_in_order(self):
        result = list()
        if self.root is not None:
            self._traverse_in_order(self.root, result)
        else:
            pass
        print(result)

    # afterorder traversing function
    def traverse_after_order(self):
        result = list()
        if self.root is not None:
            self._traverse_after_order(self.root, result)
        else:
            pass
        print(result)

    def _insert(self, tar_node, new_key):
            if new_key < tar_node.key:
                if tar_node.left_child is None:
                    tar_node.left_child = Node(new_key)
                else:
                    self._insert(tar_node.left_child, new_key)
            else:
                if tar_node.right_child is None:
                    tar_node.right_child = Node(new_key)
                else:
                    self._insert(tar_node.right_child, new_key)

    def _search(self, tar_node, tar_key):
        if tar_key < tar_node.key:
            if tar_node.left_child is None:
                return False
            else:
                return self._search(tar_node.left_child, tar_key)
        elif tar_key > tar_node.key:
            if tar_node.right_child is None:
                return False
            else:
                return self._search(tar_node.right_child, tar_key)
        else:
            return True


    def _traverse_pre_order(self, tar_node, result):
        if tar_node is not None:
            result.append(tar_node.key)
            self._traverse_pre_order(tar_node.left_child, result)
            self._traverse_pre_order(tar_node.right_child, result)
        else:
            pass

    def _traverse_in_order(self, tar_node, result):
        if tar_node is not None:
            self._traverse_in_order(tar_node.left_child, result)
            result.append(tar_node.key)
            self._traverse_in_order(tar_node.right_child, result)
        else:
            pass

    def _traverse_after_order(self, tar_node, result):
        if tar_node is not None:
            self._traverse_after_order(tar_node.left_child, result)
            self._traverse_after_order(tar_node.right_child, result)
            result.append(tar_node.key)
        else:
            pass


if __name__ == "__main__":
    debug_tree = BinarySearchTree()
    debug_tree.random_fill(100)
    debug_tree.traverse_in_order()
    print(debug_tree.search(50))
