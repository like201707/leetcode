class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romd = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        value = 0
        if 'IV' in s or 'IX' in s:
            value -= 2
        if 'XL' in s or 'XC' in s:
            value -= 20
        if 'CD' in s or 'CM' in s:
            value -= 200
        for i in s:
            value += romd[i]
        return value
