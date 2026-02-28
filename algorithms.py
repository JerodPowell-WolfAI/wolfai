"""
A module containing basic algorithm implementations: binary search and bubble sort.
"""

def bubble_sort(arr: list) -> list:
    """
    Sorts a given list in ascending order using the bubble sort algorithm.
    
    Args:
        arr (list): The list of elements to sort.
        
    Returns:
        list: The sorted list.
    """
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr


def binary_search(arr: list, target: int) -> int:
    """
    Searches for a specific target value in a sorted list using binary search.
    
    Args:
        arr (list): A sorted list of elements.
        target: The value to search for.
        
    Returns:
        int: The index of the target if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1
    
    # Loop until the pointers cross
    while low <= high:
        mid = (low + high) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
            
        # If target is greater, ignore the left half
        elif arr[mid] < target:
            low = mid + 1
            
        # If target is smaller, ignore the right half
        else:
            high = mid - 1
            
    # Target value not found
    return -1
