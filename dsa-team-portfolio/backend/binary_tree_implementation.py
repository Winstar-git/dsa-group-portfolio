from .binary_tree import Node, BinaryTree

class BinaryTreeManager:
    """Binary tree manager for web interaction."""

    def __init__(self):
        self.tree = BinaryTree()

    def add_node(self, parent_value, side, new_value):
        """Add a node to the tree."""
        if self.tree.root is None:
            # If no root exists, new_value becomes root
            self.tree.root = Node(new_value)
            return f"Root node '{new_value}' added."
        
        parent_node = self.find_node(parent_value)
        if not parent_node:
            return f"Parent node '{parent_value}' not found."

        if side.lower() == "left":
            if parent_node.left is None:
                self.tree.insert_left(parent_node, new_value)
                return f"Node '{new_value}' added to left of '{parent_value}'."
            else:
                return f"Left child of '{parent_value}' already exists."
        elif side.lower() == "right":
            if parent_node.right is None:
                self.tree.insert_right(parent_node, new_value)
                return f"Node '{new_value}' added to right of '{parent_value}'."
            else:
                return f"Right child of '{parent_value}' already exists."
        else:
            return "Side must be 'left' or 'right'."

    def find_node(self, value):
        """Return node object with the given value."""
        return self._find_node_recursive(self.tree.root, value)

    def _find_node_recursive(self, current, value):
        if current is None:
            return None
        if current.value == value:
            return current
        left_search = self._find_node_recursive(current.left, value)
        if left_search:
            return left_search
        return self._find_node_recursive(current.right, value)

    def get_tree_dict(self):
        """Return the tree as a nested dict for templates."""
        return self._node_to_dict(self.tree.root)

    def _node_to_dict(self, node):
        if node is None:
            return None
        return {
            "value": node.value,
            "left": self._node_to_dict(node.left),
            "right": self._node_to_dict(node.right)
        }
