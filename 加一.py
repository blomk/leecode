class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=len(digits)
        num=0
        for i in range (0,s):
        	num += digits[i]*(10**(s-i-1))
        digits=list(str(num+1))
        new_digits=[]
        for n in digits:
        	new_digits.append(int (n))
        return new_digits