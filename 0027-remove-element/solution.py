class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k=0
        for i in range(0,len(nums)):
            if(nums[i]!=val):
                nums[k]=nums[i]
                k=k+1
            else:
                continue
        return k  