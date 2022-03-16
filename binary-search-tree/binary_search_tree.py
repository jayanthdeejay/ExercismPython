class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = TreeNode(tree_data[0])
        for i in range(1, len(tree_data)):
            self.addNode(self.root, tree_data[i])
            
    def addNode(self, node, data):
        if(int(node.data) >= int(data)):
            if(node.left is None):
                node.left = TreeNode(data)
            else:
                self.addNode(node.left, data)
        else:
            if(node.right is None):
                node.right = TreeNode(data)
            else:
                self.addNode(node.right, data)
        

    def data(self):
        return self.root

    def sorted_data(self):
        self.data = []
        self.traverse(self.root, self.data)
        return self.data

    def traverse(self, node, data):
        if(node.left):
            self.traverse(node.left, data)
        data.append(node.data)
        if(node.right):
            self.traverse(node.right, data)
