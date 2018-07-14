class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ss = []
        if len(nums) < 3 or min(nums) > 0 or max(nums) <0:
            return ss
        elif min(nums) == 0 and max(nums) ==0:
            return [nums[:3]]
        L = len(nums)
        nums.sort()
        for i in range(L-1):
            if nums[i] <=0:
                if nums[i+1] >= 0:
                    rec = i
                    break

        for i in range(0, rec+2):
            for j in range(i+2, L):
                if nums[j] < 0:
                    continue
                for k in range(i+1, j):
                    if nums[i] + nums[j] + nums[k] == 0:
                        s = [nums[i], nums[k], nums[j]]
                        if s not in ss:
                            ss.append(s)
        return ss
