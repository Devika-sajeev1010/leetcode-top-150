class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_lower = s.lower()
        text = "".join(filter(unicode.isalnum, s_lower))
        text1 = text[::-1]
        if(text1 == text):
            return True
        else:
            return False
        