class Node:
    """A node in a binary tree."""
    def __init__(self, value,left=None, right=None):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """A binary search tree data structure with ordering property."""
    def __init__(self):
        self.root = None

    def insert(self, node, data):
        if node is None:
            return Node(data)
        else:
            if data < node.value:
                node.left = self.insert(node.left, data)
            elif data > node.value:
                node.right = self.insert(node.right, data)
        return node


    def search(self, node, target):
        """Add search function here"""
        return None
        

    def get_min_value(self, node):
        """Find the minimum value in the BST (leftmost node)."""
        if node is None:
            return None
        current = node
        while current.left is not None:
            current = current.left
        return current.value

    def preorder_traversal(self, start,traversal):
        """Traverse the tree in preorder (root, left, right)."""
        if start:
            traversal += (str(start.value) + " ")
            traversal = self.preorder_traversal(start.left,traversal)
            traversal = self.preorder_traversal(start.right,traversal)
        return traversal    

    def inorder_traversal(self, start,traversal):
        """Traverse the tree in inorder (left, root, right)."""
        if start:
            traversal = self.inorder_traversal(start.left,traversal)
            traversal += (str(start.value) + " ")
            traversal = self.inorder_traversal(start.right,traversal)
        return traversal    

    def postorder_traversal(self, start,traversal):
        """Traverse the tree in postorder (left, right, root)."""
        if start:
            traversal = self.postorder_traversal(start.left,traversal)
            traversal = self.postorder_traversal(start.right,traversal)
            traversal += (str(start.value) + " ")
        return traversal
    
    def delete(node, value):
        """ Add delete function here"""
        pass

    def get_max_value(node):
        """Add get max value function here"""
        return None

    def find_height(node):
        """Add Height of a node function here"""
        return None


# Example usage
if __name__ == "__main__":
   
    bst = BinarySearchTree()
    
        # Insert values
    values = [50, 30, 70, 20, 40, 60, 80]
    print("Inserting values:", values)
    for val in values:
        bst.root = bst.insert(bst.root, val)


        # Display traversals
    print("\nInorder traversal (sorted):", bst.inorder_traversal(bst.root,""))
    # print("Preorder traversal:", bst.preorder_traversal(bst.root,""))
    # print("Postorder traversal:", bst.postorder_traversal(bst.root,""))

      # Search for values
    print("\nSearch for 40:", bst.search(bst.root,40))
    print("Search for 25:", bst.search(bst.root,25))
    
    # Get minimum value
    print("\nMinimum value:", bst.get_min_value(bst.root))

