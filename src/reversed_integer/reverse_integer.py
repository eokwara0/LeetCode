class Solution:
    def reverse(self, x: int) -> int:

        num = -1 * x if x < 0 else x
        reversed_num = 0

        while num != 0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num = num//10

        reversed_num = -1 * reversed_num if x < 0 else reversed_num
        if reversed_num > 2147483647 or reversed_num < -2**31:
            return 0
        return reversed_num


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverse(1534236469))
