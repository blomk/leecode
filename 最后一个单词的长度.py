class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        s=s.strip()
        if not s:
        	return 0
        new_s=s[::-1]
        while i <= len(new_s)-1:
            if new_s[i] != ' ':
                i += 1
            else:
                break
        return i