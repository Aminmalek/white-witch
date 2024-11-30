from cache_service import CacheService


def main():
    # Initialize the CacheService
    cache = CacheService()

    print("Welcome to WhiteWitch Cache System!")
    while True:
        print("\nOptions:")
        print("1. Set a key-value pair")
        print("2. Get a value by key")
        print("3. Delete a key")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            ttl = int(input("Enter the TTL (in seconds): "))
            try:
                cache.set(key, value, ttl)
                print(f"Key '{key}' set successfully.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '2':
            key = input("Enter the key: ")
            try:
                value = cache.get(key)
                if value is None:
                    print(f"Key '{key}' not found or has expired.")
                else:
                    print(f"Value for key '{key}': {value}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '3':
            key = input("Enter the key to delete: ")
            try:
                cache.delete(key)
                print(f"Key '{key}' deleted successfully.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '4':
            print("Exiting WhiteWitch. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
