class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            output = strs[0]

        if strs == []:
            output = ""

        else:
            output = ''
            j = 0
            Flag = True
            try:
                while Flag:
                    tmp = 0
                    for i in range(len(strs)):
                        if strs[i] == "":
                            return ""
                        elif strs[0][j] == strs[i][j]:
                            tmp += 1
                    if tmp == len(strs):
                        output += strs[0][j]
                        j += 1
                    else:
                        Flag = False
            except IndexError:
                pass
        return output
