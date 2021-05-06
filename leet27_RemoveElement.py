# 方法一： 双指针
from typing import List

class Solution1(object):
    def removeElement(self, nums: List[int], val: int) -> int:
        a = b = 0

        while b < len(nums):
            if nums[b] != val:
                nums[a] = nums[b]
                a += 1
            b += 1
        return a

if __name__ == "__main__":
    num = [1, 2, 3, 2, 4]
    n = 2
    s = Solution1()
    l = s.removeElement(num, n)
    print("The number is: ", n, "The List is: ", num[:l])