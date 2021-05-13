class Solution(object):
    def length0fLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针， 初始值为-1， 字符串左边界，还未移动
        rk = -1
        # 记录长度
        ans = 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk +1] not in occ:
                # 不断移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符串
            ans = max(ans, rk - i +1)
        return ans

# Hash只用一次遍历
class Solution1(object):
    def length0fLongestSubstring(self, s: str) -> int:
        k, res, c_dict = -1, 0, {}
        for i, c in enumerate(s):
            # 重复时
            # c_dict > k 一个字符的情况不再继续比较 减少计算
            if c in c_dict and c_dict[c] > k:
                k = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i - k)
        return res


if __name__ == '__main__':
    s = "abcabcbb"
    sol = Solution1()
    w = sol.length0fLongestSubstring(s)
    print("The answer is :", w)
