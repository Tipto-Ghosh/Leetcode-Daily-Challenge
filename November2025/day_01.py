from typing import List , Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self , val = 0 , next = None):
        self.val = val
        self.next = next
        
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # convert the array into a set for accessing values in constant time
        nums_set = set(nums)
        # new linked list head
        new_head , prev_node = None , None 
        
        curr = head
        while curr:
            if curr.val not in nums_set: # if curr val is not in nums_set
                node = ListNode(val = curr.val)  # create a new node
                if new_head is None: # if head is emtpy then make the head
                    new_head = node 
                    prev_node = node # also set prev to new head/node 
                else:
                    prev_node.next = node # if we already have head,then just add new node to text
                    prev_node = prev_node.next # also move the prev_node to next node
            
            curr = curr.next # go to next node
        
        return new_head