from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        data = []
        nums.sort()
        array_len = len(nums)

        for i in range(array_len):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = array_len - 1

            T = 0 - nums[i]

            while j < k:

                s = nums[j] + nums[k]
                if s > T:
                    k -= 1
                elif s < T:
                    j += 1
                else:
                    data.append([-T, nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return data


if __name__ == "__main__":
    # data = [-1, 0, 1, 2, -1, -4]
    data3 = [-2, 0, 1, 1, 2]
    # data2 = [-14, -3, 11, -3, 12, -1, 11, 13, 5, 6, -11, -14, -6, 11, -4, -15, 3, -15, 9, -10, 13, -10, -9, -13, -12, 12, -7, 12, 12, 3, 9, 5, -14, -3, 9, 13, 11, 5, 3, -6, -12, -1, -5, -3, -4, -2, -10, 6, -10, 14, 3, -11, 11, 10, -9, 7, -1, -9, 4, -12, 2, -
    #          2, 8, 3, 3, -6, -7, -1, 6, 12, 8, 9, -12, 10, -8, -1, -7, -3, 12, -9, -12, 1, -5, 6, -12, -7, -2, 2, -8, -13, 5, 9, -7, -10, -3, 11, -1, -3, -13, -10, -14, 11, 6, -10, 6, 13, 4, 7, -13, -6, 13, 12, 10, -15, 4, 13, -7, 9, -8, 0, 4, 4, -6, 12, 9, -2, 0]
    solution = Solution()
    print(solution.threeSum(data3))
