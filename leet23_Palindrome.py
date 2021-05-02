class Solution(object):
    # 方法一：直接反转队列
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            s = list(str(x))
            print(s.pop())
            s_c = s.copy()
            s_c.reverse()
            if s == s_c:
                return True
            else:
                return False

    # 方法二：双向队列
    # 复杂度： O(n^2)
    def isPalindrome1(self, x: int) -> bool:
        lst = list(str(x))
        while len(lst) > 1:
            if lst.pop(0) != lst.pop():
                return False
            else:
                return True

    # 前面2种没有考虑到x=0的情况
    # 方法三：双指针
    # 复杂度：O(n)
    def isPalindrome2(self, x: int) -> bool:
        lst = list(str(x))
        L, R = 0, len(lst) - 1
        while L < R:
            if lst[L] != lst[R]:
                return False
            L += 1
            R -= 1
        return True

    # 方法四：使用log计算位数
    # 复杂度：O(n)
    def isPalindrome3(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            import math
            # 这个地方有问题 round(math.log(x, 10)) + 1 输出的L不对
            length = round(math.log(x, 10)) + 1
            L = length - 1
            print("L = ", L)
            for i in range(length//2):
                if x // 10**L != x % 10:
                    return False
                x = (x % 10**L) // 10
                L -= 2
            return True

    # 方法五：不使用log，不转成字符串
    def idPalindrome4(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        elif x == 0:
            return True
        else:
            reverse_x = 0
            while x > reverse_x:
                remainder = x % 10
                reverse_x = reverse_x * 10 + remainder
                x //= 10
            # 包含回文数为偶数和奇数2种情况
            if reverse_x == x or reverse_x // 10 == x:
                return True
            else:
                return False

    def isPalindrome5(self, x):
        return str(x) == str(x)[::-1]

if __name__ == "__main__":
    a = 1221
    print(a//10)
    s = Solution()
    print(s.isPalindrome5(a))