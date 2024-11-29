from typing import Any, Optional

from avl_tree import AVLTree


class CacheService:
    def __init__(self):
        self.avl_tree = AVLTree()

    def set(self, key: str, value: Any, ttl: int) -> None:
        self.avl_tree.insert(key, value, ttl)

    def get(self, key: str, token: str) -> Optional[Any]:
        return self.avl_tree.search(key)

    def delete(self, key: str, token: str) -> None:
        self.avl_tree.delete(key)

