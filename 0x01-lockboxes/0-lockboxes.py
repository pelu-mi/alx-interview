#!/usr/bin/python3
""" Module for lockboxes interview practice
"""


def canUnlockAll(boxes):
    """ Function to check if boxes can be unlocked
    """
    # Store all accessible boxes in a list
    keys = boxes[0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys:
                keys.append(box)
    # Check if all avaiable boxes are stored in keys
    for i in range(1, len(boxes)):
        if (i in keys):
            continue
        else:
            return False
    return True
