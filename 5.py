class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        res=needle in haystack
        if res:
            return haystack.index(needle)
        return -1