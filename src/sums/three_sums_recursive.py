from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        data = []
        for i in range(len(nums)):
            self.find_sums_of_zero(nums[i], i, nums)

    def find_sums_of_zero(self, element: int, element_index: int, sub_array: List[int]):
        pass


if __name__ == "__main__":
    data = [-1, 0, 1, 2, -1, -4]
    # data2 = [-14, -3, 11, -3, 12, -1, 11, 13, 5, 6, -11, -14, -6, 11, -4, -15, 3, -15, 9, -10, 13, -10, -9, -13, -12, 12, -7, 12, 12, 3, 9, 5, -14, -3, 9, 13, 11, 5, 3, -6, -12, -1, -5, -3, -4, -2, -10, 6, -10, 14, 3, -11, 11, 10, -9, 7, -1, -9, 4, -12, 2, -
    #  2, 8, 3, 3, -6, -7, -1, 6, 12, 8, 9, -12, 10, -8, -1, -7, -3, 12, -9, -12, 1, -5, 6, -12, -7, -2, 2, -8, -13, 5, 9, -7, -10, -3, 11, -1, -3, -13, -10, -14, 11, 6, -10, 6, 13, 4, 7, -13, -6, 13, 12, 10, -15, 4, 13, -7, 9, -8, 0, 4, 4, -6, 12, 9, -2, 0]
    solution = Solution()
    print(solution.threeSum(data))
