
# this is for understanding the heap functions
# reference : https://www.geeksforgeeks.org/dsa/binary-heap/

from heapq import heapify, heapreplace


class MinHeap:
    heaparr = []
    capacity = 0
    curr_size = 0

    heapify

    def __init__(self, size: int):
        self.capacity = size

    def swap_pos(self, loc_a: int, loc_b: int):
        temp = self.heaparr[loc_a]
        self.heaparr[loc_a] = self.heaparr[loc_b]
        self.heaparr[loc_b] = temp

    # key refers to array location of the node you need the parent of 
    def get_parent(self, key: int) -> int:
        return (key - 1) // 2
    
    def get_left(self, key: int) -> int:
        return (2 * key) + 1
    
    def get_right(self, key: int) -> int:
        return (2 * key) + 2
    
    def insert_in_heap(self, val: int) -> bool:
        if self.curr_size == self.capacity:
            return False

        i = self.curr_size        
        self.heaparr[i] = val
        self.curr_size += 1

        while i != 0 and self.heaparr[i] < self.heaparr[self.get_parent(i)]:
            i_parent = self.get_parent(i)
            self.swap_pos(i, i_parent)
            i = i_parent
        
        return True
    
    def get_min(self) -> int:
        return self.heaparr[0]
    
    def min_heapify(self, key: int):
        left = self.get_left
        right = self.get_right

        smallest = key

        if left < self.curr_size and self.heaparr[left] < self.heaparr[smallest]:
            smallest = left
        
        if right < self.curr_size and self.heaparr[right] < self.heaparr[smallest]:
            smallest = right
        
        if smallest != key:
            self.swap_pos(key, smallest)
            self.min_heapify(smallest)

    def extract_min(self) -> int:
        if self.curr_size == 0:
            return 0
        
        if self.curr_size == 1:
            self.curr_size -= 1
            return self.heaparr[0]
        
        root = self.heaparr[0]

        self.heaparr[0] = self.heaparr[self.curr_size-1]
        self.curr_size -= 1
        self.min_heapify(0)

        return root