# 方法一：双指针 fast slow
from typing import List

class Solution(object):
    def removeDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

if __name__ == "__main__":
    l = [1, 1, 2, 2, 2, 3, 3, 4]
    s = Solution()
    a = s.removeDuplicate(l)
    print("The length is:", a, ", The array is: ", l[:a])

