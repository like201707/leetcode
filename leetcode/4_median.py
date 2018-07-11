class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        new = sorted(nums1 + nums2)
        if len(new)%2 == 0:
            return (new[len(new)/2-1]+new[len(new)/2])/2.0
        else:
            return new[len(new)/2]
