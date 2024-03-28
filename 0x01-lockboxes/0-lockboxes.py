def canUnlockAll(boxes):
    """
    Checks if all the boxes can be opened using the available keys.

    Args:
        boxes: A list of lists, where each sublist
        represents the keys a box contains.

    Returns:
        True if all boxes can be opened, False otherwise.
    """

    opened = set([0])  # Start with the first box being opened

    for box in range(len(boxes)):
        if box not in opened:
            continue  # Skip already opened boxes

        for key in boxes[box]:
            if key < len(boxes):  # Check if the key is within the box range
                opened.add(key)

    return len(opened) == len(boxes)  # if opened set size matches total boxes
