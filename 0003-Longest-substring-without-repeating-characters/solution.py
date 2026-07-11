class Solution(object):
    def lengthOfLongestSubstring(self, s):
        chars = set()
        left = 0
        maxi = 0

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            chars.add(s[right])
            maxi = max(maxi, right - left + 1)

        return maxi