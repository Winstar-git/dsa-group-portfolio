from typing import List, Dict, Any, Optional
try:
	from .binary_search_tree import BinarySearchTree
except ImportError:
	from binary_search_tree import BinarySearchTree

class DictionarySearch:

	def __init__(self) -> None:
		self.bst = BinarySearchTree()

	def add_word(self, word: str) -> str:
		self.bst.root = self.bst.insert(self.bst.root, word)
		return f"Word '{word}' added successfully."

	def search_word(self, word: str) -> Dict[str, Any]:
		path: List[Any] = []
		node = self.bst.root

		while node is not None:
			path.append(node.value)
			if node.value == word:
				break
			if node.value > word:
				node = node.left
			else:
				node = node.right

		found = self.bst.search(self.bst.root, word)
		return {"found": found, "path": path}

	def delete_word(self, word: str) -> str:
		existed = self.search_word(word)["found"]
		self.bst.root = self.bst.delete(self.bst.root, word)
		if existed:
			return f"Word '{word}' deleted successfully."
		return f"Word '{word}' not found. No deletion performed."

	def get_all_words(self) -> List[str]:
		traversal_str = self.bst.inorder_traversal(self.bst.root, "")
		if not traversal_str:
			return []
		return traversal_str.strip().split()
	
	def delete_all(self) -> str:
		"""Deletes all words from the dictionary by resetting the BST root."""
		self.bst.root = None
		return "All words deleted successfully. The dictionary is now empty."

	def get_max_word(self) -> Optional[str]:
		"""Returns the maximum word in the dictionary. Returns None if the dictionary is empty."""
		return self.bst.get_max_value(self.bst.root)

	def get_min_word(self) -> Optional[str]:
		"""Returns the minimum word (lexicographically smallest) in the dictionary. 
		Returns None if the dictionary is empty."""
		return self.bst.get_min_value(self.bst.root)

__all__ = ["DictionarySearch"]

if __name__ == "__main__":
	# Small example test program
	ds = DictionarySearch()
	words_to_add = ["mango", "apple", "banana", "zebra", "cherry", "date"]
	print("Adding words:")
	for w in words_to_add:
		print(" ", ds.add_word(w))

	print("\nAll words (sorted):", ds.get_all_words())

	# Search tests
	for target in ["banana", "fig", "apple"]:
		res = ds.search_word(target)
		print(f"\nSearch '{target}': found={res['found']}, path={res['path']}")

	# Delete test
	print("\n", ds.delete_word("mango"))
	print("All words after deletion:", ds.get_all_words())


