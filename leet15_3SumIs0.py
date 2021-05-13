from typing import List
# 排序 + 双指针
class Solution(object):
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()

        # 枚举a
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c对应指针初始化最右端
            third = n - 1  # 对应最右端
            target = -nums[first]
            # 枚举b
            for second in range(first + 1, n):
                # second要和上一次不同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # b在c的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        return ans

if __name__ == '__main__':
    s = [-1,0,1,2,-1,-4]
    a = Solution()
    print(a.threeSum(s))
