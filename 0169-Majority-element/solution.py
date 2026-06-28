class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq ={}
        for key in nums:
            if key not in freq:
                freq[key] = 1
            else:
                freq[key] += 1

        maxi = sorted(freq.items() , key = lambda x:x[1] , reverse = True)
        return maxi[0][0]

        
        