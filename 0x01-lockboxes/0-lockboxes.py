def canUnlockAll(boxes):
    # Create a set to keep track of unlocked boxes
    unlocked = set([0])
    # Create a queue for breadth-first search, starting with box 0
    queue = [0]
    
    while queue:
        # Get the current box from the queue
        current_box = queue.pop(0)
        # Iterate over the keys in the current box
        for key in boxes[current_box]:
            # If the key corresponds to a box we haven't unlocked yet, unlock it and add it to the queue
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                queue.append(key)
    
    # If the number of unlocked boxes equals the total number of boxes, return True
    return len(unlocked) == len(boxes)
