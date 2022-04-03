def TowerOfHanoi(num, src, dest, aux):
    if num == 0:
        return # if the number is 0 (there are no disks) just return 0 (null) and do nothing.
    TowerOfHanoi(num-1, src, aux, dest) # Move the disk from the source rod (A) to the auxiliary rod (B).

    # print(f"Move disc {num} from {src} to {dest}")
    TowerOfHanoi(num-1, aux, dest, src) # Move the disk from the auxiliary rod (B) to the destination rod (C).
    return print(f"Move disc {num} from {src} to {dest}") # Printing where to move the disk to win.

""" 
The first argument means the number of disks.
The second argument is the starting point.
The third argument is the destination.
The fourth  argument is the auxiliary rod.
"""
# TowerOfHanoi(number_of_disks, 'A', 'C', 'B') 

TowerOfHanoi(3, 'A', 'C', 'B')