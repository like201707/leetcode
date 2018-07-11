class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        if L < 1:
            return 0
        j = 0
        for i in range(L):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j+1
