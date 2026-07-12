from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        need = Counter(t)
        window = {}

        required = len(need)
        formed = 0

        left = 0
        start = 0
        min_len = float("inf")

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                c = s[left]
                window[c] -= 1

                if c in need and window[c] < need[c]:
                    formed -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]