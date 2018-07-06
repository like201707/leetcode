class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        strx = str(x)
        bx = ''
        if strx[0] == '-':
            return False
        else:
            for i in strx[::-1]:
                bx += i
            if int(bx) == x:
                return True
            else:
                return False

        
