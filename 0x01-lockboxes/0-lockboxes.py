#!/usr/bin/python3
"""Determines if all the boxes can be opened."""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Args:
        boxes (list of lists): A list of lists representing locked boxes and keys.
    
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    # Set to keep track of unlocked boxes
    unlocked_boxes = {0}

    # Iterate over each box and its keys
    for position, box in enumerate(boxes):
        keys = set(box)  # Convert keys to a set for efficient lookup
        # If all keys needed to open the box are already unlocked or the box is the first box, mark it as unlocked
        if position in unlocked_boxes or position == 0 or keys & unlocked_boxes:
            unlocked_boxes |= keys  # Update the set of unlocked boxes with the keys
            if len(unlocked_boxes) == len(boxes):
                return True  # All boxes are unlocked
    return False  # Some boxes cannot be unlocked
