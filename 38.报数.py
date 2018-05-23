class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        last = self.countAndSay(n - 1)
        ln, res, count = last[0], '', 0
        for _ in last:
            if _ != ln:
                res += str(count) + ln
                count = 0
            count += 1
            ln = _
        res += str(count) + ln
        return res