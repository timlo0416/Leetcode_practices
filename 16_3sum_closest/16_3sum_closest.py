class Solution(object):

    nums = [-1, 2, 1, -4]
    target = 1

    def threeSumClosest(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sorted_nums = sorted(nums)
        nums_len = len(nums)
        closest = 100000
        ans = 0
        for idx, i in enumerate(sorted_nums):
            if idx > 0 and sorted_nums[idx-1] == i:
                continue
            left = idx + 1
            right = nums_len - 1
            while left < right:
                temp = i + sorted_nums[left] + sorted_nums[right]
                if temp - target > 0:
                    right -= 1
                elif temp - target < 0:
                    left += 1
                else:
                    return target
                if abs(temp - target) < closest:
                    closest = abs(temp - target)
                    ans = temp

        return ans

    threeSumClosest(nums, target)
