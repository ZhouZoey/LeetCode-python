# 方法一：暴力求解
class Solution(object):
    def reverse(self, x: int) -> int:
        # 小于10的数直接输出本身
        if -10 < x < 10:
            return x
        str_x = str(x)
        # 数字末尾不为0
        if str_x[0] != "-":
            # str_x[::-1]
            # a[开始截取位置：结束截取位置；步长]
            str_x = str_x[::-1]
            x = int(str_x)
        else:
            str_x = str_x[:0:-1]
            x = int(str_x)
            x = -x
        return x if -2147483648 < x < 2147483648 else 0

    def reverse_better(self, x: int) -> int:
        y, res = abs(x), 0
        #  (1<<31) -1: 1左移31位，相当于2^31，再-1即为上限
        boundary = (1<<31) - 1 if x > 0 else 1<<31
        while y !=0:
            # 将res整体提高一个十分位，再取y的个位数相加
            res = res*10 + y%10
            if res > boundary:
                return 0
            y //= 10
        return res if x > 0 else -res



if __name__ == "__main__":
    a = 12300
    s = Solution()
    print(s.reverse_better(a))

