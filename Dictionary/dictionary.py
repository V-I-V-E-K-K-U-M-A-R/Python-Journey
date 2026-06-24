"""
This script demonstrates the usage of Python dictionaries.

A dictionary is a mutable, ordered collection of key-value pairs.
Keys must be unique and immutable (e.g., strings, numbers, tuples).
"""


def demonstrate_accessing():
    """Shows how to access items from a dictionary."""
    print("\n--- Accessing Items ---")
    capitals = {"USA": "Washington DC", "India": "New Delhi", "China": "Beijing"}
    print(f"Original dictionary: {capitals}")

    # Using .get() is safe because it returns None for missing keys
    india_capital = capitals.get("India")
    print(f"The capital of India is: {india_capital}")

    japan_capital = capitals.get("Japan")
    print(f"The capital of Japan is: {japan_capital}")

    # You can also provide a default value for .get()
    default_value = "not found"
    japan_capital_default = capitals.get("Japan", default_value)
    print(f"The capital of Japan (with default) is: {japan_capital_default}")


def demonstrate_updating():
    """Shows how to add or update items in a dictionary."""
    print("\n--- Updating Items ---")
    capitals = {"USA": "Washington DC", "India": "New Delhi", "China": "Beijing"}
    print(f"Original dictionary: {capitals}")

    # Add a new key-value pair
    capitals.update({"Germany": "Berlin"})
    print(f"After adding Germany: {capitals}")

    # Update an existing value
    capitals.update({"India": "Newer Delhi"})
    print(f"After updating India: {capitals}")


def demonstrate_removing():
    """Shows how to remove items from a dictionary."""
    print("\n--- Removing Items ---")
    capitals = {"USA": "Washington DC", "India": "New Delhi", "China": "Beijing"}
    print(f"Original dictionary: {capitals}")

    # Remove a specific item by key using pop()
    removed_item = capitals.pop("USA")
    print(f"Removed '{removed_item}' using pop('USA'). Dictionary is now: {capitals}")

    # Remove the last inserted item using popitem()
    last_item = capitals.popitem()
    print(f"Removed '{last_item}' using popitem(). Dictionary is now: {capitals}")

    # Clear all items from the dictionary
    capitals.clear()
    print(f"After clear(): {capitals}")


def demonstrate_iteration():
    """Shows different ways to iterate over a dictionary."""
    print("\n--- Iterating Over a Dictionary ---")
    capitals = {"USA": "Washington DC", "India": "New Delhi", "China": "Beijing"}

    print("\nIterating over keys:")
    for country in capitals.keys():
        print(country)

    print("\nIterating over values:")
    for capital in capitals.values():
        print(capital)

    print("\nIterating over key-value pairs (items):")
    for country, capital in capitals.items():
        print(f"The capital of {country} is {capital}")


if __name__ == "__main__":
    demonstrate_accessing()
    demonstrate_updating()
    demonstrate_removing()
    demonstrate_iteration()