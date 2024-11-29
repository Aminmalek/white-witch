from datetime import datetime, timedelta
from typing import Optional, Any


class AVLNode:
    def __init__(self,
                 key: str,
                 value: Any = None,
                 ttl: Optional[int] = None):
        self.key = key
        self.value = value
        self.ttl = datetime.now() + timedelta(seconds=ttl) if ttl else None
        self.height: int = 1
        self.left: Optional[AVLNode] = None
        self.right: Optional[AVLNode] = None

    def is_expired(self) -> bool:
        return self.ttl is not None and datetime.now() > self.ttl


class AVLTree:
    def __init__(self):
        self._root: Optional[AVLNode] = None

    def _get_height(self, node: Optional[AVLNode]) -> int:
        return node.height if node else 0

    def _update_height(self, node: AVLNode) -> None:
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _rotate_right(self, y: AVLNode) -> AVLNode:
        x = y.left
        y.left = x.right
        x.right = y
        self._update_height(y)
        self._update_height(x)
        return x

    def _rotate_left(self, x: AVLNode) -> AVLNode:
        y = x.right
        x.right = y.left
        y.left = x
        self._update_height(x)
        self._update_height(y)
        return y

    def _get_balance(self, node: Optional[AVLNode]) -> int:
        return self._get_height(node.left) - self._get_height(node.right)

    def insert(self, key: str, value, ttl: Optional[int] = None) -> None:
        self._root = self._insert_node(self._root, key, value, ttl)

    def _insert_node(self, node: Optional[AVLNode], key: str, value, ttl: Optional[int]) -> AVLNode:
        if not node:
            return AVLNode(key, value, ttl)

        if key < node.key:
            node.left = self._insert_node(node.left, key, value, ttl)
        elif key > node.key:
            node.right = self._insert_node(node.right, key, value, ttl)
        else:
            node.value = value
            node.ttl = datetime.now() + timedelta(seconds=ttl) if ttl else node.ttl
            return node

        self._update_height(node)

        balance = self._get_balance(node)

        # Left-Left case
        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)

        # Right-Right case
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)

        # Left-Right case
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right-Left case
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def search(self, key: str) -> Any:
        node = self._root
        while node:
            if node.is_expired():
                self.delete(node.key)
                return None
            if key == node.key:
                return node.value
            node = node.left if key < node.key else node.right
        return None

    def delete(self, key: str) -> None:
        self._root = self._delete_node(self._root, key)

    def _delete_node(self, node: Optional[AVLNode], key: str) -> Optional[AVLNode]:
        if not node:
            return None

        if key < node.key:
            node.left = self._delete_node(node.left, key)
        elif key > node.key:
            node.right = self._delete_node(node.right, key)
        else:
            # Node with only one child or no child
            if not node.left or not node.right:
                return node.left or node.right

            # Node with two children: get the inorder successor (smallest in the right subtree)
            min_larger_node = self._get_min(node.right)
            node.key = min_larger_node.key
            node.value = min_larger_node.value
            node.ttl = min_larger_node.ttl
            node.right = self._delete_node(node.right, min_larger_node.key)

        self._update_height(node)

        # Rebalance the node
        balance = self._get_balance(node)

        # Left-Left case
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)

        # Right-Right case
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)

        # Left-Right case
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right-Left case
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _get_min(self, node: AVLNode) -> AVLNode:
        while node.left:
            node = node.left
        return node
