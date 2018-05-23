class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result=''
        if not strs:
        	return result
        for i in range(0,len(strs[0])):
        	temp=strs[0][i]
        	for x in strs[1:]:
        		if i > len(x)-1 or x[i] != temp:
        			return result
        	result += temp
        return result