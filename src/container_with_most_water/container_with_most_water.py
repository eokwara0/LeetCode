from typing import *


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_container = 0
        i = 0
        j = len(height)-1

        while i < j:
            number_of_rows = j - i
            left = height[i]
            right = height[j]
            right_count = number_of_rows * right
            left_count = number_of_rows * left

            if left > right:
                if right_count > max_container:
                    max_container = right_count
                j -= 1
            elif right > left:
                if left_count > max_container:
                    max_container = left_count
                i += 1
            elif right == left:
                if left_count > max_container or right_count > max_container:
                    max_container = max([left_count, right_count])
                i += 1
        return max_container


if __name__ == '__main__':
    data = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    data2 = [1, 1]
    so = Solution()
    result = so.maxArea(data)
    print(result)
