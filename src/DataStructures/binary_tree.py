class Node:
    left = None
    right = None
    count = 0
    data: float = None

    def __init__(self, data):
        self.data = data

class BinaryTree:
    root = None

    def __init__(self, data):
        self.root = Node(data)

    def _find_min_node(self, node):
        if node.left is None:
            return node.data
        return self._find_min_node(node.left)

    def _find_max_node(self, node):
        if node.right is None:
            return node.data
        return self._find_max_node(node.right)

    def _insert_node(self, node, current):
        if current.data < node.data:
            if node.left is None:
                node.left = current
            else:
                self._insert_node(node.left, current)
        elif current.data > node.data:
            if node.right is None:
                node.right = current
            else:
                self._insert_node(node.right, current)
        else:
            node.count += 1

    def _remove_node(self, node, data):
        if node is None:
            return None
        elif data < node.data:
            node.left = self._remove_node(node.left, data)
            return node
        elif data > node.data:
            node.right = self._remove_node(node.right, data)
            return node
        else:
            if node.count > 0:
                node.count -= 1
                return None

            if node.left is None and node.right is None:
                node = None
                return node
            
            if node.left is None:
                temp = node.right
                node = None
                return temp

            if node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self._find_min_node(node.right)
            node.data = temp.data

            node.right = self._remove_node(node.right, temp.data)
            return node

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            self._insert_node(self.root, node)

    def remove(self, data):
        self.root = self._remove_node(self.root, data)

    def get_root(self):
        return self.root.data

    def get_min(self):
        return self._find_min_node(self.root)

    def get_max(self):
        return self._find_max_node(self.root)

    def DFS_in_order(self):
        result = []

        def traverse(node):
            if node.left is not None:
                traverse(node.left)
            result.append(node.data)
            if node.right is not None:
                traverse(node.right)

        traverse(self.root)
        return result

    def DFS_pre_order(self):
        result = []

        def traverse(node):
            result.append(node.data)
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)

        traverse(self.root)
        return result

    def DFS_post_order(self):
        result = []

        def traverse(node):
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
            result.append(node.data)

        traverse(self.root)
        return result

    def BFS(self):
        result = []
        queue = [self.root]

        while len(queue) > 0:
            current = queue.pop(0)
            result.append(current.data)

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

        return result