# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        
        # TODO: Use slow/fast pointers to find middle
        # Hint: Move slow by 1, fast by 2
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Split the list into two halves
        second = slow.next  # Start of second half
        slow.next = None    # End first half
        
        # Step 3: Reverse the second half
        second = self.reverseList(second)
        
        # Step 4: Merge the two halves alternately
        first = head
        while second:
            # Save next nodes before we break the links
            tmp1 = first.next
            tmp2 = second.next
            
            # Reorder: first → second → tmp1
            first.next = second
            second.next = tmp1
            
            # Move pointers forward
            first = tmp1
            second = tmp2
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev


        