class Solution:
    def canJump(self, nums):
        farthest = 0

        for i in range(len(nums)):
            # If we cannot reach this index
            if i > farthest:
                return False

            # Update maximum reachable position
            farthest = max(farthest, i + nums[i])

            # If last index is reachable
            if farthest >= len(nums) - 1:
                return True

        return False