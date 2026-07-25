class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None

        oldToNew = {}

        # Pass 1: Create copy of every node
        curr = head
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next

        # Pass 2: Connect next and random pointers
        curr = head
        while curr:
            copy = oldToNew[curr]
            copy.next = oldToNew.get(curr.next)
            copy.random = oldToNew.get(curr.random)
            curr = curr.next

        return oldToNew[head]