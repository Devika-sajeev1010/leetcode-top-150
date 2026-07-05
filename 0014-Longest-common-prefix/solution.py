class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        for ch in strs:
            i=0
            while i < len(ch) and i< len(prefix) and ch[i] == prefix[i]:
                i+=1
            prefix = prefix[:i]
        return prefix


        