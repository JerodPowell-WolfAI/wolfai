from algorithms import bubble_sort, binary_search

def example_algorithms():
    """
    Showcases the functionality of bubble_sort and binary_search algorithms.
    """
    print("--- Testing Algorithms ---")
    
    # Showcase bubble sort
    unsorted_numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original list: {unsorted_numbers}")
    
    sorted_numbers = bubble_sort(unsorted_numbers.copy())
    print(f"Sorted list: {sorted_numbers}")
    
    # Showcase binary search on the sorted list
    target = 25
    index = binary_search(sorted_numbers, target)
    print(f"Searching for {target} in sorted list: Found at index {index}")
    
    target_missing = 100
    index_missing = binary_search(sorted_numbers, target_missing)
    print(f"Searching for {target_missing} in sorted list: Found at index {index_missing}")

def main():
    """
    The main method serves as the entry point to showcase functionality.
    """
    example_algorithms()

if __name__ == "__main__":
    main()