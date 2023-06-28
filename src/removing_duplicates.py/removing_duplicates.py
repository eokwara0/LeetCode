from typing import *


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        match = []

        i = 1
        j = len(nums) - 1
        cursor = nums[0]

        match.append([nums[0], i-1])
        while i <= j:
            if nums[i] == cursor:
                i += 1
            else:
                cursor = nums[i]
                match.append([nums[i], i])
                i += 1
        match_length = len(match)
        for i in range(j + 1):
            if i > match_length - 1:
                nums[i] = None
            else:
                nums[i] = match[i][0]
        print(nums)
        return match_length


if __name__ == "__main__":
    sol = Solution()
    result = sol.removeDuplicates([1, 1, 2])
    print(result)
