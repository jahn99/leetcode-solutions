class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        n = 0

        for i in range(len(nums)):
            if k== 0:
                n = nums[i]
            if nums[i] == n:
                k += 1
            else:
                k -= 1
        return n