class Solution(object):
    def deleteDuplicates(self, head):

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:

            # Duplicate found
            if curr.next and curr.val == curr.next.val:

                # Skip all nodes with this value
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next

                prev.next = curr.next

            else:
                prev = prev.next

            curr = curr.next

        return dummy.next