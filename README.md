# **WhiteWitch**

WhiteWitch is a lightweight in-memory cache system implemented in pure Python. It uses an AVL tree for efficient storage and retrieval of data and supports TTL (Time-To-Live) for automatic expiration of cache entries.
---

## **Features**
- **Efficient Data Storage**: Uses an AVL tree to ensure balanced storage and fast operations.
- **Time-To-Live (TTL)**: Allows setting a TTL for cache entries to expire automatically after a defined duration.
- **CRUD Operations**: Supports basic cache operations:
  - `set(key, value, ttl)`
  - `get(key)`
  - `delete(key)`
- **Pure Python**: No external dependencies, making it easy to integrate into Python-based projects.

---

## **Requirements**
- Python 3.7 or higher

---

## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/whitewitch.git
   cd whitewitch
   python3 main.py

## **Code Structure**

whitewitch/
│
├── cache_service.py        # Implements the cache service logic
├── avltree.py              # Implements the AVL tree structure with TTL
├── main.py                 # Example usage of the cache service
├── README.md               # Documentation for the project
