class Solution:

    nums = [3,0,-2,-1,1,2]

    def threeSum(nums):
        ans = []
        nums_len = len(nums)
        if len(nums) < 3:
            return ans
        sorted_nums = sorted(nums)
        cnt = 0
        for idx, i in enumerate(sorted_nums):
            if idx > 0 and sorted_nums[idx-1] == i:
                continue
            cnt += 1
            left = idx + 1
            right = nums_len -1
            while left < right:                
                if i + sorted_nums[left] + sorted_nums[right] > 0:
                    right -= 1
                elif i + sorted_nums[left] + sorted_nums[right] < 0:
                    left += 1
                else:
                    ans.append([i, sorted_nums[left], sorted_nums[right]])
                    left += 1
                    while sorted_nums[left] == sorted_nums[left-1] and left < right:
                        left += 1
                    right -= 1
                    while sorted_nums[right] == sorted_nums[right+1] and left < right:
                        right -= 1
        return ans
    threeSum(nums)