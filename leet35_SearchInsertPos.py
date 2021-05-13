from typing import List

# 方法一：暴力求解
class Solution(object):
    def searchInsert(self, nums: List[int], target: int) -> int:
       length = len(nums)
       for i in range(length):
            if target <= nums[i]:
                break
            else:
                i += 1
       return i

# 方法二： 二分查找法
class Solution2(object):
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high ) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return low

if __name__ == "__main__":
    nums = [1, 3, 4, 5, 6]
    n = 7
    s = Solution2()
    print("The position is: ", s.searchInsert(nums, n))