class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sx = str(x)
        counter = 0
        for i in range(len(sx)):
            if sx == '0':
                return 0
                break
            if sx[-1-i] == '0':
                counter += 1
                continue
            if sx[0] == '-':
                a = sx[1:(len(sx)-counter)] + '-' 
                if int("".join(a[::-1])) < -2147483648:
                    return 0
                else:
                    return int("".join(a[::-1]))
                
            else:
                a = sx[:(len(sx)-counter)]
                if int("".join(a[::-1])) > 2147483647:
                    return 0
                else:
                    return int("".join(a[::-1]))
