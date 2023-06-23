from typing import List
import sys
import data

sys.setrecursionlimit(20000)
# Two Sum
# Given an array of integers nums and an
# integer target, return indices of the two
# numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


class Solution:
    def twoSum(self, nums: List[int], target: int):

        for a, b in enumerate(nums):
            for (c, d) in enumerate(nums[a + 1:]):

                if d + b == target:
                    return [a, c + a + 1]

    def twoSum_(self, nums: List[int], target: int):
        return self.second_funct(nums, target, 0)

    def second_funct(self, nums: List[int], target: int, index: int):
        if index == len(nums):
            return []
        el = nums[index]
        answer = self.find(el, nums[index:], target, index, index)
        if len(answer) != 0:
            return answer
        return self.second_funct(nums, target, index + 1)

    def find(self, element: int, sub_array: List[int], target: int, el_index: int, original_index: int):
        if sub_array == []:
            return []
        if element + sub_array[0] == target and el_index != original_index:
            return [original_index, el_index]
        return self.find(element, sub_array[1:], target, el_index + 1, original_index)


if __name__ == '__main__':
    sol = Solution()
    result = sol.twoSum_(data.data, 19999)
    print(result)
