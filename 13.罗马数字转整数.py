roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ints = [roman[_] for _ in s]
        last = 1000
        total = 0
        for i in ints:
            total += i
            if i > last:
                total -= last + last
            last = i

        return total