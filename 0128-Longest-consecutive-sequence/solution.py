class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # Check if it's the start of a sequence
            if num - 1 not in numSet:
                current = num
                length = 1

                while current + 1 in numSet:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest