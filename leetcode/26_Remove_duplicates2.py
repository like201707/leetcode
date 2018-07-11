class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nl = []
        for num in nums:
            if num not in nl:
                nl.append(num)

        nums[:len(nl)] = nl[:]
        return len(nl)
