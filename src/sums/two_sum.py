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
        end = len(nums)-1

        for i in range(end + 1):

            j = i + 1
            k = end

            while j <= k:
                s = nums[j] + nums[i]
                w = nums[k] + nums[i]
                if s == target:
                    return [i, j]
                elif w == target:
                    return [i, k]
                j += 1
                k -= 1


if __name__ == '__main__':
    sol = Solution()
    result = sol.twoSum(data.data, 19999)
    print(result)
