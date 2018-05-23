class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result=int(str(abs(x))[::-1])
        if x > 0:
        	result = result
        else:
        	result = -result
        if result > 2147483647 or result < -2147483647:
        	return 0
        return result