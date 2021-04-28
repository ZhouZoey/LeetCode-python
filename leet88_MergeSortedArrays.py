from typing import List

# Method1： Merged then sorted
class Solution(object):
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()
        return nums1

# Method2: 双指针 从头比
class Solution1(object):
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        sorted = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:
                sorted.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                sorted.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                sorted.append(nums1[p1])
                p1 += 1
            else:
                sorted.append(nums2[p2])
                p2 += 1
        nums1[:] = sorted
        return nums1

# Method3: 逆向双指针
# 取两数比较较大的数放在nums1的尾部
class Solution2():
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2 = m - 1, n - 1

        tail = m + n - 1
        while p1 > 0 or p2 > 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1
            print(nums1)
        return nums1

# 和第三种方法一样，代码实现不一样
class Solution3():
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while m >= 0 and n >= 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]


if __name__ == "__main__":
    s1 = [1, 2, 3, 5]
    s2 = [2, 4, 6, 8, 9]
    m = 4
    n = 4
    a = Solution2()
    print(a.merge(s1, m, s2, n))
